# Generated by Django 4.2.5 on 2023-10-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taller_Mecanico', '0008_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
