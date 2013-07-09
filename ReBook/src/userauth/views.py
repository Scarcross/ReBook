# Create your views here.
from django.shortcuts import render_to_response


def login(request):
    return render_to_response('userauth/login.html')

def logout(request):
    return render_to_response('userauth/logout.html')

