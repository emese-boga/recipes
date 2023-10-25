from django.db import models
from uuid import uuid4


MEDIUM_TEXT = 80


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=MEDIUM_TEXT)
