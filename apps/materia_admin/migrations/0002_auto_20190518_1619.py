# Generated by Django 2.0 on 2019-05-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia_admin',
            name='Dia2',
            field=models.CharField(blank=True, choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('Domingo', 'Domingo')], max_length=20, null=True),
        ),
    ]
