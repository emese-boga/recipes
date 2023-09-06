from django.db import models
from uuid import uuid4


MEDIUM_TEXT = 80


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=MEDIUM_TEXT)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    instructions = models.TextField()