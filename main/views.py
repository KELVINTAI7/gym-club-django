from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def classes(request):
    return render(request, 'classes.html')
def trainers(request):
    return render(request, 'trainers.html')
def contact(request):
    return render(request, 'contact.html')