from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
    def __init__(self,nombre,apellido): #Constructor
        self.nombre=nombre
        self.apellido=apellido


def despedida(request):
    documento="Chay mundo con Django."
    return HttpResponse(documento)


def calculaEdad(request,edad,anhoFuturo):
    #edadActual=26
    periodo=anhoFuturo-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años</h2></body></html>" %(anhoFuturo, edadFutura) 
    return HttpResponse(documento)


def ejemplo3(request):
    ejemplo3="<html><body><h1>Ejemplo 3 con Django<h1></body></html>"
    return HttpResponse(ejemplo3)


def ejemplo4(request):
    ejemplo4="""<html>
    <body>
    <h1>
    Ejemplo 4 con Django
    <h1>
    </body>
    </html>"""
    return HttpResponse(ejemplo4)


def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""
    <html>
    <body>
    <h1>
    Fecha & hora actuales: %s
    <h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)


def saludo(request):
    temas_2=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    p1=Persona("Valentina","d'Andria")
    nombre="Ever"
    ahora=datetime.datetime.now()
    doc_externo=open("D:/Google Drive/dev/technologies/django/Pildoras/Proyecto1/plantillas/miplantilla.html")
    plantilla=Template(doc_externo.read())
    doc_externo.close()
    contexto=Context({"clave_diccionario":nombre, "apellido_persona":"Ruiz Diaz", "fecha":ahora,"novia_nombre":p1.nombre, "novia_apellido":p1.apellido, "temas":["Italia","Japon","Tesla","Perro","Tango"],"temon":temas_2}) #Contexto & ClaveDiccionario {}
    documento=plantilla.render(contexto)
    return HttpResponse(documento)