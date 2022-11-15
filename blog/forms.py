from django import forms
from blog.models import Usuario

class UsuarioForm(forms.ModelForm):
#    fecha_de_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%y"], 
#       widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'fecha_de_nacimiento')

    