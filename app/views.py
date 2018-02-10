from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from mastodon import Mastodon
import os

MASTODON_BASE_URL = os.environ['MASTODON_BASE_URL']
CLIENT_ID = os.environ['CLIENT_ID'] 
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['REDIRECT_URI']


# Create your views here.
def index(request):
    access_token = request.COOKIES.get('access_token')
    print(access_token)
    if access_token == None:
        print("true")
        return redirect("/login")    
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def redirect2auth(request):
    return HttpResponse("リダイレクト中です...")

def redirected(request):
    return HttpResponse(str(request.POST))