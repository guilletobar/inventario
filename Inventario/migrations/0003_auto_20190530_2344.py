# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-31 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='descripcion',
            field=models.TextField(max_length=20),
        ),
    ]
