from django.shortcuts import render, get_object_or_404
from django.views import View
from blog.forms import UsuarioForm, Buscar
from django.urls import reverse_lazy
from blog.models import Usuario, Post
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

class ListarUsuarios(View):
    template_name = "blog/lista_de_usuarios.html"

    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, self.template_name, {"usuarios": usuarios})


class CargarUsuarios(View):
    template_name = "blog/carga_de_usuarios.html"
    form_class = UsuarioForm
    initial = {"nombre": "", "apellido":"", "fecha_de_nacimiento":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form":form})

class ActualizarUsuarios(View):
    template_name = "blog/actualizar_usuarios.html"
    success_template = "blog/exito.html"
    form_class = UsuarioForm
    initial = {"nombre": "", "apellido":"", "fecha_de_nacimiento":""}

    def get(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        form = self.form_class(instance=usuario)
        return render(request, self.template_name, {"form": form, "pk":pk})

    def post(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        form = self.form_class(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.success_template)

class BuscarUsuario(View):

    form_class = Buscar
    template_name = 'blog/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_usuarios = Usuario.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'lista_usuarios':lista_usuarios})
        return render(request, self.template_name, {"form": form})

def index(request):
    return render(request, 'blog/index.html')

class UsuarioList(ListView):
    model = Usuario

class UsuarioCrear(CreateView):
    model = Usuario
    success_url = "/panel-usuario"
    fields = ["nombre", "apellido", "fecha_de_nacimiento"]

class UsuarioBorrar(DeleteView):
    model = Usuario
    success_url = "/panel-usuario"

class UsuarioActualizar(UpdateView):
    model = Usuario
    success_url = "/panel-usuario"
    fields = ["nombre", "apellido", "fecha_de_nacimiento"]


class ListPost(ListView):
    model=Post

class CreatePost(CreateView):
    model=Post
    fields = ['title', 'short_content', 'content']
    success_url = reverse_lazy("list-post")

class DetailPost(DetailView):
    model=Post

class UpdatePost(UpdateView):
    model=Post
    fields=['title', 'short_content', 'content']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)