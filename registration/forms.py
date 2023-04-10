from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, label="First Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    mob_no = forms.CharField(min_length=10, max_length=10, label="Contact Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="New Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirm Password")

    models.User._meta.get_field('email')._unique = True
    
    class Meta:
        model = models.User
        fields = ( "first_name", "last_name", "username" , "email", "mob_no", )
