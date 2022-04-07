from django.urls import reverse
from django.shortcuts import render,redirect
import random
from django.http import HttpResponse
from urlapp.models import UrlData
import string
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return render(request, "login_form.html")

@csrf_exempt
def login_user_view(request):
    username= request.POST['username']
    password= request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect("/home")
    return HttpResponse("Invalid Credential!")

def home(request):
    if request.user.is_authenticated:
        urls = UrlData.objects.filter(user = request.user.id).all()
        return render(request,'home.html', {'urls' : urls})
    else:
        return render(request,"home.html")
    
def createshorturl(request):
    if request.method == 'POST':
        slug = ''.join(random.choice(string.ascii_letters)
                        for x in range(10))
        url = request.POST["url"]
        if request.user.is_authenticated:
            if UrlData.objects.filter(url=url, user=request.user.id).exists():
                urls = UrlData.objects.filter(user = request.user.id).all()
                return render(request,'home.html', {'urls':urls, 'status' : 'true'})
            else:
                new_url = UrlData(url=url, slug=slug, user=request.user)
                new_url.save()
            return redirect('/home')
        else:
            new_url = UrlData(url=url, slug=slug, user=None)
            new_url.save()
            return render(request,'home.html', {'long_url':url, 'slug' : slug})


def urlRedirect(request, slugs):
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)

def logout_view(request):
    logout(request)
    return redirect('/')

