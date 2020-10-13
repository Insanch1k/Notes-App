from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

'''Create a model for Notes'''


class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Changes(models.Model):
    changed_note = models.IntegerField()
    version = models.IntegerField(default=1)
    content = models.TextField()
    title = models.CharField(max_length=50)
    changed_at = models.DateTimeField(default=timezone.now)
