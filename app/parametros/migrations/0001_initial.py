# Generated by Django 2.2 on 2019-06-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstaCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombEsCi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombEtni', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiEs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLogro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiLo', models.CharField(max_length=50)),
            ],
        ),
    ]
