from unicodedata import name
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name="profile"),
]