# Generated by Django 3.1.7 on 2021-04-10 22:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_auto_20210410_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 4, 10, 22, 46, 19, 557839, tzinfo=utc)),
        ),
    ]