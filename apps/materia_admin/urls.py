
from django.conf.urls import url, include
from apps.materia_admin.views import *

urlpatterns = [
    
   
    url(r'inicio', index, name='inicio'),

    url(r'nuevo',materia_view, name='nuevo'),



]