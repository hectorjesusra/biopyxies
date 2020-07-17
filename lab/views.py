from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'lab/about.html')

def apps(request):
    return render(request, 'lab/apps.html')

def tutorial(request):
    return render(request, 'lab/tutorial.html')
