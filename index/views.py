from django.shortcuts import render, redirect


def index_view(request, *args, **kwargs):
    if(is_logged_in(request)):
        return redirect("/landing")
    
    return redirect("/login")
# Create your views here.

def is_logged_in(request):
    user = request.user
    return user.is_authenticated