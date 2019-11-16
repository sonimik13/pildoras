from django.db import models


# En el parametro de la clase Project hereda model.Model
# Esto arma como si fuera una tabla de BD 
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo") #Cadena de caracteres 
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificacion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    # Metodo reservado lleva doble guionbajo en ambos lados..    
    def __str__(self): # Esto es para que devuelva una cadena & no un objets
        return self.title