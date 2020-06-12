# Generated by Django 2.0 on 2019-05-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia_admin', '0002_auto_20190518_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia_admin',
            name='Dia1',
            field=models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('Domingo', 'Domingo'), ('.', '')], max_length=20),
        ),
        migrations.AlterField(
            model_name='materia_admin',
            name='Dia2',
            field=models.CharField(blank=True, choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('Domingo', 'Domingo'), ('.', '')], default='.', max_length=20, null=True),
        ),
    ]