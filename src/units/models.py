from django.db import models


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=16)
    unit_type = models.CharField(max_length=32)
