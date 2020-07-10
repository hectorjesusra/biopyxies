from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    content={'name':'Hector','age':18}
    return render(request, 'index.html',content)

def about(request):

    return render(request, 'about.html')

def lab(request):

    return render(request, 'lab.html')

def contact(request):

    return render(request, 'contact.html')

def forum(request):

    return render(request, 'forum.html')
