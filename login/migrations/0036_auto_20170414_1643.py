# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import draceditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0035_auto_20170411_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=draceditor.models.DraceditorField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='details',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
