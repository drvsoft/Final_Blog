from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return f" ID: {self.id} Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha Nac.: {self.fecha_de_nacimiento}"



class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"