# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-12 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170405_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userform',
            name='case_type',
        ),
    ]
