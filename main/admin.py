from django.contrib import admin
from .models import Note
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(Note, SimpleHistoryAdmin)
