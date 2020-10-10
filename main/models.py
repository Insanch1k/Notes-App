from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
'''Create a model for Notes'''


class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title


'''
class Changes(models.Model):
    note = models.ForeignKey(Note)
    changed_data = models.TextField()
    changed_at = models.DateTimeField(default=timezone.now)
'''
