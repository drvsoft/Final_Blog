from django.shortcuts import render, get_object_or_404
from django.views import View
from blog.forms import UsuarioForm
from blog.models import Usuario

def index(request):
    return render(request, 'blog/index.html')

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




