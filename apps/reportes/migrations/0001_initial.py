# Generated by Django 3.1.7 on 2021-04-06 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos', '0001_initial'),
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
                ('estado_inicial', models.CharField(max_length=15)),
                ('estado_final', models.CharField(max_length=15)),
                ('cant_horas_invertidas', models.IntegerField()),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.contrato')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.empleado')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.registrohora')),
            ],
        ),
    ]
