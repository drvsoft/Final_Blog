from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return f" ID: {self.id} Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha Nac.: {self.fecha_de_nacimiento}"