from django.db import models

from uuid import uuid4


MEDIUM_TEXT = 80
LONG_TEXT = 256


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=MEDIUM_TEXT, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=LONG_TEXT)
    instructions = models.TextField()
