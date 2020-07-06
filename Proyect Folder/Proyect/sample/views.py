from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    n=6000
    list=[x**2 for x in range(n) if x%2==0]
    text="["
    for i in list:
        text=text+str(i)+', '
    text=text+']'
    return HttpResponse(f"The list of numbers is {text}")
