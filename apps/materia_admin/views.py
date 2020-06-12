from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from django.http import HttpResponse
from datetime import date

from apps.materia_admin.forms import MateriaForms
from apps.materia_admin.models import *
# Create your views here.

#metodo para agregar registros  a la base de datos
def materia_view(request):
	if request.method == 'POST':
		form = MateriaForms(request.POST)
		if form.is_valid() :
			form.save()
		return redirect('index')
	else:	
	     form=MateriaForms()
	fecha=date.today().year	 
	return render(request,'secciones/form_new_seccion.html',{'form':form,"fecha":fecha})  


# metodo para listar registros
def index(request):
	seccion =Materia_admin.objects.order_by("Materia")
	fecha=date.today().year
	contexto ={'secciones':seccion, "fecha":fecha}
	return render(request, 'secciones/index.html',contexto)	   	

#editar registro
def editar(request,seccion):
	seccion=Materia_admin.objects.get(id = seccion)
	fecha=date.today().year
	if request.method== 'GET':
		form = MateriaForms(instance= seccion) 
	else:
		form = MateriaForms(request.POST,instance=seccion)
		if form.is_valid():
			form.save()
		return redirect('index')	
	return render(request,'secciones/form_new_seccion.html',{'form':form,"fecha":fecha}) 

#Metodo para llamar acerca de 
def about(request):
	pass
	return render(request,'Base/about.html')

#esta es la funcion para ver el registro completo.
def seccion_view(request,seccion):
	fecha=date.today().year
	seccion=get_object_or_404(Materia_admin,id= seccion)
	if request.method == 'POST':
		pass
		seccion = MateriaForms(instance= seccion) 
	
		
	return render(request,'secciones/form_presentacion.html',{'seccion':seccion,"fecha":fecha}) 
"""def buscar(request,var):
	seccion_buscada = get_object_or_404(Materia_admin,seccion=var)
	contexto ={
		"seccion_buscada":seccion_buscada
	}	

	return render(request,"seccion/form_presentacion.html",contexto)
"""

def handler404(request):
    response = render_to_response('seccion/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('seccion/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response	