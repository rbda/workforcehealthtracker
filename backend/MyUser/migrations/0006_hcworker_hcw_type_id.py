# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-26 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyUser', '0005_hcwtype_resultstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='hcworker',
            name='hcw_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyUser.HCWType'),
            preserve_default=False,
        ),
    ]