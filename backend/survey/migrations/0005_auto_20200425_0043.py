# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-24 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20200401_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyinstance',
            name='sent_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='surveyinstance',
            name='submitted_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='surveyinstance',
            name='survey_date',
            field=models.DateTimeField(null=True),
        ),
    ]
