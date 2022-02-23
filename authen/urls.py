from django.urls import path
from .views import logout_request,sigup_view
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="authen/login.html"), name="login"), 
    path('logout/', logout_request,name='logout'), 
    path('sigup/', sigup_view,name='sigup'), 
]
