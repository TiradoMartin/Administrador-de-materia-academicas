from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.materia_admin.forms import MateriaForms
from apps.materia_admin.models import *
# Create your views here.

#metodo para agregar registros  a la base de datos
def materia_view(request):
	if request.method == 'POST':
		form = MateriaForms(request.POST)
		if form.is_valid() :
			form.save()
		return redirect('inicio')
	else:	
	     form=MateriaForms()
	return render(request,'secciones/form_new_seccion.html',{'form':form})  


# metodo para listar registros
def index(request):
	seccion =Materia_admin.objects.all()
	contexto ={'secciones':seccion}
	return render(request, 'secciones/index.html',contexto)	   	

#editar registro
def editar(request,seccion):
	seccion=Materia_admin.objects.get(id = seccion)
	if request.method== 'GET':
		form = MateriaForms(instance= seccion) 
	else:
		form = MateriaForms(request.POST,instance=seccion)
		if form.is_valid():
			form.save()
		return redirect('inicio')	
	return render(request,'secciones/form_new_seccion.html',{'form':form}) 
