from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("This is the home section")
    content={'name':'Hector','age':18}
    return render(request, 'index.html',content)

def about(request):
    #return HttpResponse("This is the about section")
    return render(request, 'about.html')

def lab(request):
    #return HttpResponse("This is the lab section")
    return render(request, 'lab.html')

def contact(request):
    #return HttpResponse("This is the contact section")
    return render(request, 'contact.html')

def forum(request):
    #return HttpResponse("This is the forum section")
    return render(request, 'forum.html')
