# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-24 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyweatherbycity',
            name='new_york_temp',
        ),
        migrations.RemoveField(
            model_name='monthlyweatherbycity',
            name='san_franciso_temp',
        ),
    ]
