# Generated by Django 3.1.7 on 2021-04-06 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=30)),
                ('tarifa_gs', models.FloatField()),
                ('tarifa_ds', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=60)),
                ('estado_final', models.CharField(max_length=15)),
                ('costo', models.FloatField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.area')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=80)),
                ('fecha_nacimiento', models.DateField()),
                ('tarifa', models.FloatField(default=0)),
                ('estado', models.CharField(default='Activo', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.cargo')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
