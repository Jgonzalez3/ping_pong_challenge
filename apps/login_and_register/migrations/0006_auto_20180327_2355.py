# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_register', '0005_auto_20180327_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='skill',
            field=models.IntegerField(default=1),
        ),
    ]