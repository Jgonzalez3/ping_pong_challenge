# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simgame', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]