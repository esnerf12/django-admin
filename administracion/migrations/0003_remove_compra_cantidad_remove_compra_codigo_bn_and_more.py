# Generated by Django 5.1 on 2024-09-03 16:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_articulo_codigo_bn_alter_articulo_marca_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='codigo_bn',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='fecha_adq',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='placa',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='tipo_articulo',
        ),
        migrations.AddField(
            model_name='asignacion',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='averia',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='articulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administracion.articulo'),
            preserve_default=False,
        ),
    ]
