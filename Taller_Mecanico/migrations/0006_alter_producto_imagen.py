# Generated by Django 4.2.5 on 2023-09-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taller_Mecanico', '0005_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
