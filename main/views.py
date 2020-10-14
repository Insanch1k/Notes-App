from .models import Note, Changes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import NotesSerializer, ChangesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

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


'''Function for updating a note and create a new version of note'''


@api_view(['POST'])
def notes_update(request, pk):
    try:
        note = Note.objects.get(id=pk)
        serializer = NotesSerializer(instance=note, data=request.data)

        if serializer.is_valid(raise_exception=True):
            changes_for_this_id = Changes.objects.filter(changed_note=pk).last()
            if changes_for_this_id:
                new_update = Changes.objects.create(changed_note=pk)
                last_version = changes_for_this_id.version
                new_update.version = int(last_version) + 1
                new_update.title = note.title
                new_update.content = note.content
                new_update.save()
            else:
                new_update = Changes.objects.create(changed_note=pk)
                new_update.content = note.content
                new_update.title = note.title
                new_update.save()
            serializer.save()
    except ObjectDoesNotExist as e:
        return Response({'error': 'There is no such note'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


'''Function for delete a note'''


@api_view(['DELETE'])
def notes_delete(request, pk):
    try:
        note = Note.objects.get(id=pk)
        note.delete()
    except ObjectDoesNotExist as e:
        return Response({'error': 'There is no such note'}, status=status.HTTP_404_NOT_FOUND)
    return Response("Note successfully deleted")


'''Function for getting history of changes'''


@api_view(['GET'])
def get_changes(request, note_id):
    changes = Changes.objects.filter(changed_note=note_id)
    serializer = ChangesSerializer(changes, many=True)
    return Response(serializer.data)
