from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('authorized/', views.authorized, name='authorized'),
    path('authorized/', views.AuthorizedView.as_view(), name='authorized'),
    path('advantages/', views.AdvantagesView.as_view(), name='advantages'),
    path('login/', views.LoginInterface.as_view(), name='login'),
    path('logout/', views.LogoutInterface.as_view(), name='logout'),
]