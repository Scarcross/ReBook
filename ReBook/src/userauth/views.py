# Create your views here.
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User

def register(request,username,email,user_pw):
    if email is None:
        email = username
        
    return render_to_response('userauth/register.html')

def login(request,username,user_pw):
    if request.method == 'POST':
        user = User.objects.create_user(username, username,user_pw)
        user.save()
#  TODO:
#     return to user message if this login is valid or not
    return render(request,'login.html')
    
def logout(request):
    return render_to_response('userauth/logout.html')

def index(request):
    return render_to_response('userauth/login.html')


