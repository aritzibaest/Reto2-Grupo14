# Generated by Django 3.0.4 on 2020-04-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default=666666666, max_length=9),
            preserve_default=False,
        ),
    ]
