# Generated by Django 2.2 on 2019-06-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20190621_0644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ['nombre'], 'verbose_name': 'perfil', 'verbose_name_plural': 'perfiles'},
        ),
        migrations.AlterField(
            model_name='perfil',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(max_length=100, verbose_name='Telefono'),
        ),
    ]
