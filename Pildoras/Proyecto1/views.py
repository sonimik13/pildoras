from django.http import HttpResponse
import datetime

""" Django uses request and response objects to pass state through the system.
When a page is requested, Django creates an HttpRequest object that contains
metadata about the request. Then Django loads the appropriate view, passing 
the HttpRequest as the first argument to the view function. Each view is responsible 
for returning an HttpResponse object.

This document explains the APIs for HttpRequest and HttpResponse objects, which are 
defined in the django.http module. """
""" Creamos una vista con una funcion """
def saludo(request): # primera vista

    return HttpResponse("Hola mundo con Django.")

def despedida(request):
    documento="Chay mundo con Django."
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

# %s es un marcador de posicion.
# % en esa posicion en concreto lo que quiero.
def dameFecha(request):
    fecha_actual=datetime.datetime.now() #importar datetime
    documento="""
    <html>
    <body>
    <h1>
    Fecha & hora actuales: %s
    <h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,anhoFuturo):
    #edadActual=26
    periodo=anhoFuturo-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años</h2></body></html>" %(anhoFuturo, edadFutura) 

    return HttpResponse(documento)