# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hanzi', '0006_auto_20170616_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hanzi',
            old_name='hanzi',
            new_name='simplified',
        ),
    ]
