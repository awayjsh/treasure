from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .form import CustomUserCreationForm
from .form import CustomUserChangeForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request) :
    if request.method == 'POST' :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else :
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html',context)

def delete(request) :

    request.user.delete()
    return redirect('articles:index')

def update(request) :

    if request.method == "POST" :

        pass

    else :

        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form' : form,
    }

    return render