# Generated by Django 3.1.7 on 2021-04-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='rentabilidad',
        ),
        migrations.AddField(
            model_name='contrato',
            name='gastos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contrato',
            name='rentabilidad_horas',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='rentabilidad_presupuesto',
            field=models.FloatField(default=0, null=True),
        ),
    ]
