# Generated by Django 3.2.3 on 2021-06-30 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESIGRAD', '0016_alter_répertoire_date_création'),
    ]

    operations = [
        migrations.AlterField(
            model_name='répertoire',
            name='date_création',
            field=models.DateField(default=datetime.datetime(2021, 6, 30, 14, 26, 5, 631313)),
        ),
    ]
