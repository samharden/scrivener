# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('fl', 'Florida')], max_length=20)),
                ('county', models.CharField(choices=[('hill', 'Hillsborough'), ('pine', 'Pinellas')], max_length=20)),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('judge', models.CharField(max_length=20)),
                ('case_type', models.CharField(max_length=20)),
                ('attorney', models.CharField(max_length=20)),
                ('case_number', models.CharField(max_length=20)),
            ],
        ),
    ]
