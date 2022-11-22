"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import (ListarUsuarios, CargarUsuarios, ActualizarUsuarios, BuscarUsuario, 
                        UsuarioList, UsuarioCrear, UsuarioBorrar, UsuarioActualizar, ListPost, CreatePost,
                        DetailPost, UpdatePost, DeletePost, SearchPostByName)
from blog.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', ListarUsuarios.as_view()),
    path('usuarios/cargar/', CargarUsuarios.as_view()),
    path('usuarios/actualizar', ActualizarUsuarios.as_view()),
    path('usuarios/actualizar/<int:pk>', ActualizarUsuarios.as_view()),

    path('usuarios/buscar', BuscarUsuario.as_view()),
    path('panel-usuario', UsuarioList.as_view(), name="usuario-list"),
    path('panel-usuario/crear', UsuarioCrear.as_view(), name="usuario-crear"),
    path('panel-usuario/<int:pk>/borrar', UsuarioBorrar.as_view(), name="usuario-borrar"),
    path('panel-usuario/<int:pk>/actualizar', UsuarioActualizar.as_view(), name="usuario-actualizar"),

    path('blog/', index, name="index-blog"),
    path('panel-post/list/', ListPost.as_view(), name="list-post"),
    path('panel-post/create/', CreatePost.as_view(), name="create-post"),
    path('panel-post/detail/<int:pk>/', DetailPost.as_view(), name="detail-post"),
    path('panel-post/update/<int:pk>/', UpdatePost.as_view(), name="update-post"),
    path('panel-post/delete/<int:pk>', DeletePost.as_view(), name="delete-post"),
    path('panel-post/search-by-name/', SearchPostByName.as_view(), name="search-by-name-post"),



]
