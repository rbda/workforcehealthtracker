# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-28 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200328_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyinstance',
            name='submitted_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
