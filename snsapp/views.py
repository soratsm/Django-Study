from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

from snsapp.models import SnsModel


# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, '', password)
        except:
            return redirect('login')
    return render(request, 'signup.html')


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'context': 'not logged in'})

    return render(request, 'login.html', {'context': 'get method'})


@login_required
def listfunc(request):
    object_list = SnsModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


@login_required
def detailfunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    return render(request, 'detail.html', {'object': object})

@login_required
def goodfunc(request, pk):
    object = get_object_or_404(SnsModel, pk=pk)
    object += 1
    object.save()
    return redirect('list')
