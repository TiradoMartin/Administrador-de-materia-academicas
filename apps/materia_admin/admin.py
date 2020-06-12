from django.contrib import admin
from  apps.materia_admin.models import *

# Register your models here.

@admin.register(Materia_admin)
class Panel_materia(admin.ModelAdmin):
    list_display=("Seccion","Materia","Recinto","Profesor","Clasificacion")
    list_filter=("Seccion","Materia","Recinto","Profesor","Clasificacion","Tanda","Dia1","Publicado","Curso")

