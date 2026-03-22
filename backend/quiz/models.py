from django.db import models
from django.conf import settings
import uuid


class Question(models.Model):
    """
    Quiz question with multiple-choice answers.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    options = models.JSONField()  # list of 4 choices
    answer = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)  # easy/medium/hard
    image_url = models.URLField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.text[:50]}"


class Session(models.Model):
    """
    Completed quiz session for a user.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.score}/{self.total_questions}"


class Badge(models.Model):
    """
    Badge definition.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserBadge(models.Model):
    """
    Badge unlocked by a user.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "badge")

    def __str__(self):
        return f"{self.user} - {self.badge.slug}"

# Create your models here.
