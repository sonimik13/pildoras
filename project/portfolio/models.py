from django.db import models


# En el parametro de la clase Project hereda model.Model
# Esto arma como si fuera una tabla de BD 
class Project(models.Model):
    title = models.CharField(max_length=200) #Cadena de caracteres 
    description = models.TextField()
    image = models.ImageField()
    created =   models.DateTimeField(auto_now_add=True)
    updated =   models.DateTimeField(auto_now=True)


