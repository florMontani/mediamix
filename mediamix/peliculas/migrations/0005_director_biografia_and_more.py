# Generated by Django 5.1 on 2024-09-06 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0004_alter_director_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='Biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='director_origen_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='peliculas_director', to='peliculas.director'),
        ),
    ]
