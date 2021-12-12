from django.urls import path
from .views import login_view,sigup_view

 
urlpatterns = [
    path('login/', login_view), 
    path('sigup/', sigup_view), 
]
