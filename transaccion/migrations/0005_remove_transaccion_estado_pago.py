# Generated by Django 4.2.4 on 2024-03-20 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0004_transaccion_estado_pago_alter_transaccion_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='estado_pago',
        ),
    ]
