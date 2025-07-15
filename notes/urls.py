from django. urls import path, include

from . import views

urlpatterns = [
    # path('notes', views.notes_list, name='notes_list'),
    path('notes', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name='note_detail'),
    path('notes/popular/', views.PopularNotesListView.as_view(), name='popular_notes'),
    path('notes/create/', views.NotesCreateView.as_view(), name='notes.create'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('notes/<int:pk>/add_likes', views.add_like_view, name='notes.add_likes'),
    path('notes/<int:pk>/change_private_status', views.change_private_status, name='notes.change_private_status'),
]
