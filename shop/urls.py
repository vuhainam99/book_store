from django.urls import path
from .views import *

 
urlpatterns = [
    path('', shop_view), 
    path('detail/<int:id_book>', detail_view), 
    path('cart_now/<int:id_book>', cart_now , name='cart_now'), 
]
