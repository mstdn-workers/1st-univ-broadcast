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
DOMAIN = os.environ['DOMAIN']


# Create your views here.
def index(request):
    access_token = None
    try:
        access_token = request.get_signed_cookie('access_token')
    except:
        pass
    ms = Mastodon(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_base_url=API_BASE_URL, access_token=access_token) 
    if access_token == None:
        print("true")
        return redirect("app:login")    
    return redirect("app:broadcast")
    # return render(request, 'app/index.html')

def login(request):
    ms = Mastodon(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_base_url=API_BASE_URL)
    auth_request_url = ms.auth_request_url(redirect_uris=os.path.join(ROOT_URL, 'auth'))
    context = {
        'auth_request_url': auth_request_url,
    }
    return render(request, 'app/login.html', context)

def redirected(request):
    ms = Mastodon(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_base_url=API_BASE_URL)
    access_token = ms.log_in(code=request.GET['code'], redirect_uri=os.path.join(ROOT_URL, 'auth'))
    res = HttpResponse(access_token)
    res.set_cookie(key='access_token', value=access_token, domain=DOMAIN)
    return res
def redirected2(request):
    return HttpResponse(request.GET)

def auth(request):
    res = redirect("app:index")
    if request.GET['code'] is not None:
        ms = Mastodon(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_base_url=API_BASE_URL)
        access_token = ms.log_in(code=request.GET['code'], redirect_uri=os.path.join(ROOT_URL, 'auth'))
        # res.set_signed_cookie(key='access_token', value=access_token, domain=DOMAIN)
    return res

def broadcast(request):
    access_token = None
    try:
        access_token = request.get_signed_cookie('access_token')
    except:
        pass
    if access_token is None:
        return redirect("app:login")
    return HttpResponse("broadcast")
