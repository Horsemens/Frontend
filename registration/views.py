from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def register(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        reg_form = forms.NewUserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect("." + "?success=True")
    else:
          reg_form = forms.NewUserCreationForm()
          
    
    if (('success' in request.GET) and (request.GET["success"] == "True")) :
        context["success"] =  True
    context["form"] = reg_form
    return render(request,'register.html', context=context)