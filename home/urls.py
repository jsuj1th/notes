from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    # path('authorized/', views.authorized, name='authorized'),
    path('authorized/', views.AuthorizedView.as_view(), name='authorized'),
    path('advantages/', views.AdvantagesView.as_view(), name='advantages'),
]