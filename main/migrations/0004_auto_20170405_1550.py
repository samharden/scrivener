# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170331_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='county',
            field=models.CharField(choices=[('hill', 'Hillsborough')], max_length=20),
        ),
    ]
