# Generated by Django 4.2.4 on 2024-04-03 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pInteres', '0004_puntointeres_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puntointeres',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
