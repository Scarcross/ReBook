# Create your views here.
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.models import User
from userauth.models import RegisterForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import login
from django.utils import simplejson

def register(request):
    #Js data is just for redirect to the right anchor after a failure while logging in
    js_data = simplejson.dumps('#register')
    if request.method == 'POST':  # If the form has been submitted...
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            username = request.POST['username']
            pw = request.POST['password']
            User.objects.create_user(username, pw)
            return redirect('thanks')  # Redirect after POST
    else:
        form = RegisterForm()
    loginform = LoginForm()
    return render(request, 'registration/login.html', {'pwform':form,'form':loginform,'js_data':js_data})

def login(request):
    pwform = RegisterForm()
     #Js data is just for redirect to the right anchor after a failure while logging in
    js_data = simplejson.dumps('#login')
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
#             Authenticate if no bullshit was written
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('thanks')
                    # Redirect to a success page.
                else:
                    form.username.errors['loginerror'] += 'Login err !'
                    return render(request,'registration/login.html',{'form':form,'pwform':pwform,'js_data':js_data})
                    # Return a 'disabled account' error message
            else:
                form.errors['othererror'] = ' Other Error !'
                return render(request,'registration/login.html',{'form':form,'pwform':pwform,'js_data':js_data})
    else:
        form = LoginForm()#  TODO:
        #     return to user message if this login is valid or not
    return render(request, 'registration/login.html',{'form':form,'pwform':pwform,'js_data':js_data})

def logout(request):
    logout(request)
    return render_to_response('userauth/logout.html')

def index(request):
    return render_to_response('userauth/index.html')


def thanks(request):
    return render_to_response('userauth/thanks.html')


@login_required(login_url='userauth/userarea.html')
def userarea(request):
    if (request.user.is_authenticated()):
        return render(request,'userauth/userarea.html')
    else:
        return HttpResponseForbidden()
