from django.db import models
from django.utils import timezone
timezone.now()

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)  # 可以不填

    def __str__(self):
        return self.title