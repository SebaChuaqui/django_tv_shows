from django.db import models

class Canal(models.Model):
    nombre = models.CharField(max_length=20)

class Programa(models.Model):
    titulo = models.CharField(max_length=65)
    canal = models.ForeignKey(Canal, related_name="shows", on_delete = models.CASCADE)
    estreno = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    descripcion = models.TextField()
