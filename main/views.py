from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import Note
from rest_framework.generics import ListAPIView, RetrieveAPIView
from main.serializers import NotesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

'''Class for display all notes'''


class NotesListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer


'''Function for display a detail information about note'''


class NoteDetailView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer


'''Function for creating a new note'''


@api_view(['POST'])
def notes_create(request):
    serializer = NotesSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


'''Function for updating a note'''


@api_view(['POST'])
def notes_update(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NotesSerializer(instance=note, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


'''Function for delete a note'''


@api_view(['DELETE'])
def notes_delete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response(serializer.data)
