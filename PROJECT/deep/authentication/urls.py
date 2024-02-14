
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('insect', views.insect, name='insect'),
    path('insect1', views.insect1, name='insect1'),
    path('insect2', views.insect2, name='insect2'),

]
