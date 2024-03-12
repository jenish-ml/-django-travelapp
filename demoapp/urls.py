from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('logout',views.logout,name='logout'),
    path('add_place',views.addplace,name='add_place'),
    path('add_user',views.adduser,name='add_user'),
]