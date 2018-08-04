from django.db import models

# Create your models here.
class Blogger(models.Model):
    """
    Modelo que representa a un blogger
    """
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    ciudad = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()


    def __str__(self):
        return self.nombre + "_" + self.apellido 


class Post(models.Model):
    """
    Modelo que representa a una publicación.
    """
    titulo = models.CharField(max_length=120, blank=False, null=False)
    contenido = models.TextField(blank=False, null=False)
    publicacion = models.TimeField(auto_now_add=True)   
    blogger = models.ForeignKey('Blogger', related_name='blogger', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ["publicacion"]

    def __str__(self):
        return self.titulo