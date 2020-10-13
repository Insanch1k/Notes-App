from rest_framework import serializers

from .models import Note, Changes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created', 'modified']


class ChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Changes
        fields = ['version', 'changed_note', 'changed_at', 'title', 'content']
