from django.shortcuts import render, redirect


def index_view(request, *args, **kwargs):
    if(is_logged_in(request)):
        return redirect("/landing")
    
    return redirect("/login")
# Create your views here.

def is_logged_in(request):
    if request.session.get("is_logged_in") and request.session.get("is_logged_in") == "True":
        print(request.session["is_logged_in"])
        return True
    return False