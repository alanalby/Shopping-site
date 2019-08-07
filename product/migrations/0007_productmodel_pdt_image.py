# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_size_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='pdt_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=b''),
            preserve_default=False,
        ),
    ]