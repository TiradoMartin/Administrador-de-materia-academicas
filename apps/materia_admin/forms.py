from django import forms
from apps.materia_admin.models import Materia_admin
from ckeditor.widgets import CKEditorWidget


class MateriaForms(forms.ModelForm):
	Comentario= forms.CharField(widget = CKEditorWidget())  

	class Meta:
		model = Materia_admin
		fields = ['Seccion',
	             'Materia',
	             'Profesor',
	             'Recinto',
	             'Curso',
	             'Dia1',
	             'Dia2',
	             'hora',
	             'Tanda',
	             'Clasificacion',
	             'Comentario' 

	              ]
		labels ={'Seccion' : 'Sección ',
	             'Materia' :'Materia',
	             'Profesor' :'Profesor ',
	             'Recinto' :'Recinto',
	             'Curso' :'Curso',
	             'Dia1' : 'Primer dia de la semana',
	             'Dia2' : 'Segundo dia de la semana',
	             'hora' : 'Horario',
	             'Tanda' : 'Tanda',
	             'Clasificacion' : 'Clasificación',
	             'Comentario' : 'Comentario',


	    }


		widgets ={
	             'Seccion' :forms.TextInput(attrs={'class':'form-control'}),
	             'Materia':forms.TextInput(attrs={'class':'form-control'}),
	             'Profesor':forms.TextInput(attrs={'class':'form-control'}),
	             'Recinto' :forms.Select(attrs={'class':'form-control'}),
	             'Curso':forms.TextInput(attrs={'class':'form-control'}),
	             'Dia1':forms.Select(attrs={'class':'form-control'}),
	             'Dia2':forms.Select(attrs={'class':'form-control'}),
	             'Tanda':forms.Select(attrs={'class':'form-control'}),
	             'Clasificacion':forms.Select(attrs={'class':'form-control'}),
	             'Comentario' :forms.TextInput(attrs={'class':'form-control'}),




	    }













	    