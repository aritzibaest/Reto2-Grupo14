# Generated by Django 3.0.4 on 2020-04-13 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_cliente_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefono',
        ),
    ]
