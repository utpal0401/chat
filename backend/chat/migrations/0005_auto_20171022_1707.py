# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20171022_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
