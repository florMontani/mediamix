# Generated by Django 5.1 on 2024-09-19 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0009_peliculas_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genero',
            options={'verbose_name': 'Género', 'verbose_name_plural': 'Generos'},
        ),
    ]
