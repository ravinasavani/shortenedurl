from django.urls import path
from urlapp.views import login_view,login_user_view,home,createshorturl,urlRedirect,logout_view

urlpatterns = [
    path("", login_view, name="login"),
    path('login_user/', login_user_view, name="login_user"),
    path('logout', logout_view, name="logout"),
    path("home", home, name="home"),
    path("createshorturl", createshorturl, name="createshorturl"),
    path("u/<str:slugs>", urlRedirect, name="redirecturl")
]

