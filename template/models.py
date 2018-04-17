# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import datetime

from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'colors'
