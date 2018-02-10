from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from mastodon import Mastodon
import os
import requests

API_BASE_URL = os.environ['API_BASE_URL']
CLIENT_ID = os.environ['CLIENT_ID'] 
CLIENT_SECRET = os.environ['CLIENT_SECRET']
ROOT_URL = os.environ['ROOT_URL']


# Create your views here.
def index(request):
    access_token = request.COOKIES.get('key')
    print(access_token)
    if access_token == None:
        print("true")
        return redirect("app:login")    
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def redirect2auth(request):
    ms = Mastodon(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_base_url=API_BASE_URL)
    return redirect(ms.auth_request_url(redirect_uris=os.path.join(ROOT_URL, 'redirected')))

def redirected(request):
    ms = Mastodon(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_base_url=API_BASE_URL)
    access_token = ms.log_in(code=request.GET['code'], redirect_uri=os.path.join(ROOT_URL, 'redirected'))
    return HttpResponse(access_token)
def redirected2(request):
    return HttpResponse(request.GET['access_token'])