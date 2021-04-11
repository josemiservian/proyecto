# Generated by Django 3.1.7 on 2021-04-06 15:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('rubro', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=80)),
                ('monto', models.IntegerField()),
                ('horas_presupuestadas', models.IntegerField(default=0)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(default='Activo', max_length=15)),
                ('rentabilidad', models.IntegerField(default=0, null=True)),
                ('horas_ejecutadas', models.IntegerField(default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.cliente')),
                ('tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=80, null=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.contrato')),
                ('lider_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroHora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('detalle', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField(default=datetime.time(0, 0))),
                ('hora_fin', models.TimeField(default=datetime.time(0, 0))),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.contrato')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='MiembroEquipoProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('LPR', 'Lider del Proyecto'), ('CON', 'Consultor'), ('AUD', 'Auditor')], default='CON', max_length=3)),
                ('tarifa_asignada', models.FloatField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.empleado')),
                ('equipo_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.equipoproyecto')),
            ],
        ),
    ]
