# Generated by Django 3.2.3 on 2021-05-28 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ESIGRAD', '0005_auto_20210528_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubrique',
            name='utilisateur_admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ESIGRAD.utilisateur_admin'),
        ),
    ]