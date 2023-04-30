from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    pass
