from django.urls import path
from . import views

urlpatterns = [
    path('notes/list/', views.NotesListView.as_view(), name='notes-list'),
    path('notes/detail/<int:pk>/', views.NoteDetailView.as_view(), name='notes-detail'),
    path('notes/create/', views.notes_create, name='notes-create'),
    path('notes/update/<int:pk>/', views.notes_update, name='notes-update'),
    path('notes/delete/<int:pk>/', views.notes_delete, name='notes-delete'),
    path('notes/history/<int:note_id>/', views.get_changes, name='get-changes')
]
