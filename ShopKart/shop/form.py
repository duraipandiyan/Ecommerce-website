from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class customuserform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Enter Password Name'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Enter Confirm Password Name'}))
    class Meta:
        model=User
        # fields=["First Name","Last Name","Email","Password1","Password2"]
        fields=['username',"email",'password1','password2']