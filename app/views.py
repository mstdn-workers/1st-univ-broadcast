from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

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

def redirected(request):
    return HttpResponse(str(request.POST))