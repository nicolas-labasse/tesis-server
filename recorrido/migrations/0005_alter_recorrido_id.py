# Generated by Django 4.2.4 on 2024-03-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recorrido', '0004_alter_recorrido_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recorrido',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
