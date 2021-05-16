from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('members/',views.members,name='members'),
    path('events/',views.events,name='events'),
    path('resources/',views.members,name='resources'),
    path('blogs/',views.events,name='blogs'),
]