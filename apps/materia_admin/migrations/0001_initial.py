# Generated by Django 2.0 on 2018-02-28 04:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seccion', models.CharField(max_length=7)),
                ('Materia', models.CharField(max_length=30)),
                ('Profesor', models.CharField(max_length=30)),
                ('Recinto', models.CharField(choices=[('Utesa Santiago de los Caballeros', 'Utesa Sede Central Santiago de los Caballeros'), ('Utesa Santo Domingo', 'Utesa Santo Domingo'), ('Utesa Santo Domingo Oriental', 'Utesa Santo Domingo Oriental'), ('Utesa Puerto Plata', 'Utesa Puerto Plata'), ('Utesa Moca', 'Utesa Moca'), ('Utesa Mao', 'Utesa Mao'), ('Utesa Dajabón', 'Utesa Dajabón'), ('Utesa Escuela Graduados - Santiago', 'Utesa Escuela Graduados - Santiago '), ('Utesa Gaspar Hernández', ' Utesa Gaspar Hernández')], max_length=50)),
                ('Curso', models.CharField(max_length=11)),
                ('Dia1', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('Domingo', 'Domingo')], max_length=20)),
                ('Dia2', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('Domingo', 'Domingo')], max_length=20)),
                ('hora', models.CharField(max_length=50)),
                ('Tanda', models.CharField(choices=[('en la mañana', 'En la mañana'), ('en la tarde', 'En la tarde'), ('en la noche', 'En la noche')], max_length=30)),
                ('Clasificacion', models.CharField(choices=[('bueno', 'Bueno'), ('normal', 'Normal'), ('malo', 'Malo')], default='bueno', max_length=11)),
                ('Publicado', models.DateTimeField(auto_now_add=True)),
                ('Comentario', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
