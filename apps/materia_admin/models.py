from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Materia_admin(models.Model):
	Seccion = models.CharField(max_length=7)
	Materia = models.CharField(max_length=30)
	Profesor = models.CharField(max_length=30)
	Recinto_opc = (('Utesa Santiago de los Caballeros','Utesa Sede Central Santiago de los Caballeros'),('Utesa Santo Domingo','Utesa Santo Domingo'),('Utesa Santo Domingo Oriental','Utesa Santo Domingo Oriental'),('Utesa Puerto Plata','Utesa Puerto Plata'),('Utesa Moca','Utesa Moca'),('Utesa Mao','Utesa Mao'),('Utesa Dajabón','Utesa Dajabón'),('Utesa Escuela Graduados - Santiago','Utesa Escuela Graduados - Santiago '),('Utesa Gaspar Hernández',' Utesa Gaspar Hernández'))
	Recinto =models.CharField(max_length=50,choices=Recinto_opc)
	Curso = models.CharField(max_length=11)
	Dia_opc =(('lunes','Lunes'),('martes','Martes'),('miercoles','Miercoles'),('jueves', 'Jueves'),('viernes','Viernes'),('sabado','Sabado'),('Domingo','Domingo'))
	Dia1 = models.CharField(max_length=20,choices=Dia_opc)
	Dia2 = models.CharField(max_length=20,choices=Dia_opc)
	hora = models.CharField(max_length=50)
	Tanda_opc =(('en la mañana','En la mañana'),('en la tarde','En la tarde'),('en la noche','En la noche'))
	Tanda = models.CharField(max_length=30,choices=Tanda_opc)
	Clasificacion_opc =(('bueno','Bueno'),('normal','Normal'),('malo','Malo'))
	Clasificacion =  models.CharField(max_length=11,choices=Clasificacion_opc,default='bueno')
	Publicado = models.DateTimeField(auto_now_add=True)
	Comentario = RichTextField()

	def __str__(self):
		fecha=str(self.Publicado)

		info='seccion:'+' '+self.Seccion.upper()+' - '+'Materia:'+' '+self.Materia.title()+' '+fecha
		return info



