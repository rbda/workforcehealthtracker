# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-13 08:23
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0005_auto_20200413_1353'),
        ('groups', '0002_auto_20200401_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='facility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facility.Facility', verbose_name='Organization'),
        ),
    ]
