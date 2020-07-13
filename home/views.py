from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def lab(request):
    return render(request, 'lab.html')

def lababout(request):
    return render(request, 'lab/about.html')

def labapps(request):
    return render(request, 'lab/apps.html')

def molemule(request):
    return render(request, 'lab/apps/molemule.html')

def nucleo(request):
    return render(request, 'lab/apps/nucleo.html')

def pyteins(request):
    return render(request, 'lab/apps/pyteins.html')

def labtutorial(request):
    return render(request, 'lab/tutorial.html')

def contact(request):
    return render(request, 'contact.html')

def forum(request):
    return render(request, 'forum.html')
