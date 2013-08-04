# Create your views here.
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.models import User
from userauth.models import RegisterForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def register(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = RegisterForm(request.POST)
        print form.errors
        if(form.is_valid()):
            username = request.POST['username']
            pw = request.POST['password']
            User.objects.create_user(username, pw)
            return redirect('thanks')  # Redirect after POST
    else:
        form = RegisterForm()
    return render(request, 'userauth/register.html', {'form':form})

@login_required(login_url='userauth/login.html')
def login(request):
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
#             Authenticate if no bullshit was written
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect()
                    # Redirect to a success page.
                else:
                    form.username.errors['loginerror'] += 'you did shit !'
                    return render(request,'userauth/login.html',{'form':form})
                    # Return a 'disabled account' error message
            else:
                form.errors['othererror'] = ' Other Error !'
                return render(request,'userauth/login.html',{'form':form})
    else:
        form = LoginForm()#  TODO:
        #     return to user message if this login is valid or not
    return render(request, 'userauth/login.html',{'form':form})

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
