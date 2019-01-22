from django.urls import path
from .views import *

app_name = 'pastebin'

urlpatterns = [
    path('add', AddNote.as_view(), name='add_note'),
    path('recent_notes', RecentNotes.as_view(), name='recent_notes'),
    path('view/<int:pk>', ViewNote.as_view(), name='view_note'),
    path('update/<int:id>', UpdateNote.as_view(), name='update_note'),
    path('delete/<int:id>', deleteNote, name='delete_note'),
]