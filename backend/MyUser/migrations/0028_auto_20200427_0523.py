# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-26 23:53
from __future__ import unicode_literals

import MyUser.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUser', '0027_auto_20200426_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hcworker',
            name='date_of_birth',
            field=models.DateField(validators=[MyUser.models.HCWorker.validate_date_of_birth]),
        ),
        migrations.AlterField(
            model_name='hcworker',
            name='telegram_username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telegram username'),
        ),
    ]
