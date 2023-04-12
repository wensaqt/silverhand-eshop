from django.shortcuts import render

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

def login(request):
    return render(request, 'login.html')