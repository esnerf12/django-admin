# Generated by Django 5.1 on 2024-10-02 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_articulo_sede'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='sede',
        ),
        migrations.AddField(
            model_name='asignacion',
            name='sede',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administracion.sede'),
            preserve_default=False,
        ),
    ]
