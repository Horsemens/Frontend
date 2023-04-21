from django.shortcuts import render, redirect
from django.contrib.auth import logout as lg

# Create your views here.
def logout(request):
    lg(request)
    return redirect("/login")