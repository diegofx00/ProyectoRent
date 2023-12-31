# Generated by Django 4.2.5 on 2023-09-05 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arriendos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('idVehiculo', models.IntegerField(null=True)),
                ('idCliente', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
                ('apellidos', models.TextField(max_length=30)),
                ('rut', models.TextField(max_length=12)),
                ('telefono', models.TextField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=25)),
                ('apellido', models.TextField(max_length=25)),
                ('telefono', models.TextField(max_length=15)),
                ('cargo', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.TextField(max_length=25)),
                ('modelo', models.TextField(max_length=25)),
                ('year', models.IntegerField()),
                ('cant_vehiculos', models.IntegerField()),
            ],
        ),
    ]
