from django.shortcuts import render
from .models import Pages
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def pagina_inicio(request):
	pages = Pages.objects.all()
	respuesta = "Bienvenido a la pagina de inicio. Estos son los contenidos almacenados: <br>"
	for page in pages:
         respuesta += "<br>" + str(page.id) + ": <a href='/web/" + str(page.id) + "'>" + page.name + "</a>"

	return HttpResponse(respuesta)

def createPage(request, nombre, pagina):
    newPage = Pages(name=nombre, page=pagina)
    newPage.save()

    return HttpResponse("La pagina " + newPage.name + " ha sido añadida correctamente. <br>")

def showContent(request, identificador):
    try:
        page = Pages.objects.get(id=identificador)
        respuesta = page.page
        return HttpResponse(respuesta)
    except Pages.DoesNotExist:
        respuesta = "Page not found: /web/%d." %int(identificador) #hago esto ya que identificador es str
        return HttpResponseNotFound(respuesta)
