from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView
from .models import Note

class AddNote(CreateView):
    model = Note
    template_name = 'pastebin/AddNote.html'
    fields = ['title', 'text']

    def post(self, request, **kwargs):
        temp_note = Note()
        temp_note.title = request.POST['title']
        temp_note.text = request.POST['text']
        temp_note.save()
        return HttpResponseRedirect(reverse('pastebin:recent_notes'))

class UpdateNote(UpdateView):

    def get(self, request, id):
        form = Note.objects.get(id=id)
        return render(request, 'pastebin/UpdateNote.html', {'form':form})

    def post(self, request, id):
        temp_note = Note.objects.get(id=id)
        temp_note.title = request.POST['title']
        temp_note.text = request.POST['text']
        temp_note.save()
        return HttpResponseRedirect(reverse('pastebin:recent_notes'))

class RecentNotes(ListView):
    model = Note
    template_name = 'pastebin/RecentNotes.html'
    context_object_name = 'notes'
    def get_queryset(self):
        return Note.objects.all()

class ViewNote(DetailView):
    model = Note
    template_name = 'pastebin/ViewNote.html'
    
def deleteNote(request, id):
    Note.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('pastebin:recent_notes'))
