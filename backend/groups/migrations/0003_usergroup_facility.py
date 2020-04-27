# -*- coding: utf-8 -*-

#   Licensed to the Apache Software Foundation (ASF) under one
#   or more contributor license agreements.  See the NOTICE file
#   distributed with this work for additional information
#   regarding copyright ownership.  The ASF licenses this file
#   to you under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in compliance
#   with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing,
#   software distributed under the License is distributed on an
#   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#   KIND, either express or implied.  See the License for the
#   specific language governing permissions and limitations
#   under the License.
#
#   Built and managed with Open Source Love by BeeHyv Software Solutions Pvt Ltd. Hyderabad
#   www.beehyv.com

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
