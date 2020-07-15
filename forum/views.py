from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm
from .models import Post

@login_required(login_url='login')
def profile(request):
    return render(request, 'forum/profile.html')


@login_required(login_url='login')
def forum(request):
    context ={
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'forum/posts.html', context)

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('/forum')
    else:
        form= CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                user=form.cleaned_data.get('username')
                messages.success(request,user)

                return redirect('/forum/login')

        context={'form':form}
        return render(request, 'forum/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/forum')
    else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/forum')

            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'forum/login.html' ,context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('/forum/login')
