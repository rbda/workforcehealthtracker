# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-31 16:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyUser', '0018_hcworker_immunodeficiency'),
    ]

    operations = [
        migrations.AddField(
            model_name='hcworker',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='HC manager'),
            preserve_default=False,
        ),
    ]
