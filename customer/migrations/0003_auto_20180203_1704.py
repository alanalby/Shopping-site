# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_mywalletmodal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywalletmodal',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mywalletmodal',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]