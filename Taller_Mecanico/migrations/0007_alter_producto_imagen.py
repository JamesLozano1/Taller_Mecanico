# Generated by Django 4.2.5 on 2023-09-28 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taller_Mecanico', '0006_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]