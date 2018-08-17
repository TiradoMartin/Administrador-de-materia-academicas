"""utesasocial2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.materia_admin.views import *
from django.shortcuts import render
#url de la aplicacion
urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^acercade/', about, name='acercade'),
     url(r'^ckeditor/', include('ckeditor_uploader.urls')),
 url(r'^nuevo/', materia_view, name='nuevo'),
   url(r'^editar/(?P<seccion>\d+)/$',editar, name='editar'),
    url(r'^vista/(?P<seccion>\d+)/$',seccion_view, name='vista'),
    url(r'^', index, name='index'),
    

 #url(r'^registro', include('apps.materia_admin.urls')),
 

  # url(r'^entrar', BienvenidaView.as_view(), name='bienvenida'),

  # url(r'^registrate/', SignUpView.as_view(), name='sign_up'),

    #url(r'^incia-sesion/', SignInView.as_view(), name='sign_in'),

   # url(r'^cerrar-sesion/', SignOutView.as_view(), name='sign_out'),'''

]

admin.site.site_header = 'Administración de Graper'