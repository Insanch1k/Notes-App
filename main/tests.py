from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Note


class NotesApiTestCase(APITestCase):
    def test_get_list(self):
        url = reverse('notes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_create(self):
        url = reverse('notes-create')
        data = {'title': 'test1', 'content': 'test1'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_detail(self):
        new_note = Note.objects.create(title='test1', content='test1')
        url = reverse('notes-detail', kwargs={'pk': new_note.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_delete(self):
        new_note = Note.objects.create(title="test1", content='test1')
        url = reverse('notes-delete', kwargs={'pk': new_note.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_update(self):
        new_note = Note.objects.create(title='test1', content='test1')
        url = reverse('notes-update', kwargs={'pk': new_note.id})
        data = {'title': 'updated', 'content': 'UPDATED'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_changes(self):
        new_note = Note.objects.create(title='test1', content='test1')
        url = reverse('get-changes', kwargs={'note_id': new_note.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
