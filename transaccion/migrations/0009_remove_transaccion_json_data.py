# Generated by Django 4.2.4 on 2024-03-22 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0008_transaccion_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='json_data',
        ),
    ]
