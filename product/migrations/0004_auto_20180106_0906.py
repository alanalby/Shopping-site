# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-06 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180106_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_discrption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='sub_category_disc',
            field=models.TextField(blank=True, null=True),
        ),
    ]