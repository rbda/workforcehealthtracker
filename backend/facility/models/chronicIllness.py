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

from django.db import models
class ChronicIllness(models.Model):
    illness_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.illness_name

    class Meta:
        app_label = "facility"
        verbose_name = 'Chronic Illness'

