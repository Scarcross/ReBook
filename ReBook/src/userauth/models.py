from django import forms
# Create your models here.
class RegisterForm(forms.Form):
    username = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email Address'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Password'}))

