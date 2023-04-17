from django.shortcuts import render , redirect

# Create your views here.
def landing(request):
    if(not is_logged_in(request)):
        redirect("/login")

    if request.method == "POST":
        if request.POST.get("logout") and request.POST.get("logout") == "logout":
            request.session["is_logged_in"] = "False"
            return redirect("/login")

    return render(request,'landing_page.html')

def is_logged_in(request):
    if request.session.get("is_logged_in") and request.session.get("is_logged_in") == "True":
        print(request.session["is_logged_in"])
        return True
    return False