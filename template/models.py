import datetime

from django.db import models

from common.models import AppModel


class Color(AppModel):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'colors'
