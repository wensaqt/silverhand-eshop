from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def best_sellers(request):
    return render(request, 'best-sellers.html')

def categories(request):
    return render(request, 'categories.html')

def collections(request):
    return render(request, 'collections.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = None

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'