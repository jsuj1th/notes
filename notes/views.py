from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Notes
from .forms import NotesForm
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    form_class = NotesForm
    # template_name = 'notes/notes_create.html'
    success_url = '/smart/notes'
    
class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'text']
    form_class = NotesForm
    # template_name = 'notes/notes_update.html'
    success_url = '/smart/notes'

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    # template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    login_url = '/admin'

class NotesDeleteView(DeleteView):
    model = Notes
    # template_name = 'notes/notes_delete.html'
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    context_object_name = 'note'

class NotesAddLikesView(View):
    def post(self, request, pk):
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return redirect('/smart/notes')

class NotesDetailView(DetailView):
    model = Notes
    # template_name = 'notes/detail.html'
    context_object_name = 'note'

class PopularNotesListView(ListView):
    model = Notes
    template_name = 'notes/notes_popular_notes.html'
    context_object_name = 'notes'
    queryset = Notes.objects.filter(likes__gte=1)

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('note_detail', args=[pk]))    
    else:
        raise Http404("Invalid request method")

    # def get_queryset(self):
    #     return Notes.objects.order_by('-likes')[:5]
# def notes_list(request):
#     all_notes = models.Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = models.Notes.objects.get(pk=pk)
#     except models.Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/detail.html', {'note': note})


# def get_popular_notes(request):
#     popular_notes = models.Notes.objects.order_by('-created_at')[:5]
#     return render(request, 'notes/popular_notes.html', {'popular_notes': popular_notes})