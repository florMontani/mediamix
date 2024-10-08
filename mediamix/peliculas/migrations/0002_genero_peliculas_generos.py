# Generated by Django 5.1 on 2024-08-31 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='peliculas',
            name='generos',
            field=models.ManyToManyField(related_name='peliculas', to='peliculas.genero'),
        ),
    ]
