# Generated by Django 5.1 on 2024-10-14 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_pelicula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='fecha',
            new_name='fecha_lanzamiento',
        ),
    ]
