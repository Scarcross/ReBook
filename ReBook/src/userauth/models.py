from django.db import models
from django import forms
# Create your models here.
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    sender = forms.EmailField()
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput)
