from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

class LoginInterface(LoginView):
    template_name = 'home/login.html'
    # redirect_authenticated_user = True

class LogoutInterface(LogoutView):
    template_name = 'home/logout.html'
    next_page=None
    
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'current_time': datetime.now()}

class AuthorizedView(LoginRequiredMixin,TemplateView):
    login_url = '/admin'
    template_name = 'home/authorized.html'
    extra_context = {'current_time': datetime.now()}


class AdvantagesView(TemplateView):
    template_name = 'home/advantages.html'
# def home(request):
#     # return HttpResponse("Welcome to the Home Page")
#     return render(request, 'home/welcome.html', {'current_time': datetime.now()})

# @login_required(login_url='/admin')
# def authorized(request):
#     # return HttpResponse("You are in an authorized area")
#     return render(request, 'home/authorized.html', {'current_time': datetime.now()})