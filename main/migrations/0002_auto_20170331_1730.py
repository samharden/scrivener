# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='case_type_detail',
            field=models.CharField(default='nil', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userform',
            name='case_type',
            field=models.CharField(choices=[('crim', 'Criminal'), ('small-claim', 'Small Claims'), ('discrim', 'Discrimination')], max_length=20),
        ),
    ]
