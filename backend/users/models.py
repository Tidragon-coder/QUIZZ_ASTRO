from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    """
    Custom user storing XP and creation timestamp.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    xp = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# Create your models here.
