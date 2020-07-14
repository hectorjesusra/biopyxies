from django.shortcuts import render

# Create your views here.
def molemule(request):
    return render(request, 'lab/apps/molemule.html')

def nucleo(request):
    return render(request, 'lab/apps/nucleo.html')

def pyteins(request):
    return render(request, 'lab/apps/pyteins.html')
