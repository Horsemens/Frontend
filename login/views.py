from django.shortcuts import render , redirect
from django.contrib.auth import authenticate


# Create your views here.

def login(request):
    if(is_logged_in(request)):
        return redirect("/")

    context = {}
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        keep = request.POST.getlist('keep')
        if(len(keep) > 0):
            keep = True
        else:
            keep = False

        user = authenticate(username=username, password=password)

        if user is not None:
            request.session["is_logged_in"] = "True"
            if keep:
                request.session.set_expiry(2592000)
            return redirect("/")
        else :
            return redirect("." + "?fail=True")

    if (('fail' in request.GET) and (request.GET["fail"] == "True")) :
        context["fail"] =  True
    return render(request, 'login.html', context=context)

def is_logged_in(request):
    if request.session.get("is_logged_in") and request.session.get("is_logged_in") == "True":
        print(request.session["is_logged_in"])
        return True
    return False