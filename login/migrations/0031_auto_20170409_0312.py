# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0030_auto_20170408_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
