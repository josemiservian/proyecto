# Generated by Django 3.1.7 on 2021-04-10 18:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_auto_20210409_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 18, 16, 46, 334990, tzinfo=utc)),
        ),
    ]
