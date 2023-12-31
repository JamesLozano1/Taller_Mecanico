# Generated by Django 4.2.5 on 2023-09-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
