# Generated by Django 3.2.3 on 2021-06-30 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESIGRAD', '0020_alter_répertoire_date_création'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='emplacement',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='document',
            name='nom_doc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='document',
            name='propriétaire',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='notification',
            name='titre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rubrique',
            name='nom_rub',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='répertoire',
            name='date_création',
            field=models.DateField(default=datetime.datetime(2021, 6, 30, 16, 29, 3, 870754)),
        ),
        migrations.AlterField(
            model_name='répertoire',
            name='nom_rep',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='adresse',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='mot_de_passe',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='nom_utilisateur',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='utilisateur_admin',
            name='status',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='utilisateur_privilégié',
            name='status',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='utilisateur_simple',
            name='status',
            field=models.CharField(max_length=200),
        ),
    ]
