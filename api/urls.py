from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api.views import (API_login,Book_API,Book_details_API,List_gerses_book,Oder_book_API,add_cart,rating_api,rating_show,send_mail_buynow)


 
urlpatterns = [
 
    # path('v1/config/', API_Config), 
    path('v1/login/', API_login), 
    path('v1/book/', Book_API), 
    # path('v1/recommender/', Book_recommender_API), 
    path('v1/details/', Book_details_API), 
    path('v1/list_geres/', List_gerses_book), 
    path('v1/order/', Oder_book_API), 
    path('v1/add_cart/', add_cart), 
    path('v1/rating/', rating_api), 
    path('v1/rating_show/', rating_show), 
    path('v1/send_mail_buynow/', send_mail_buynow), 


    
]
#http://127.0.0.1:8000/api/v1/order/ method POST
#{
#    "id_user":2
#}
# http://127.0.0.1:8000/api/v1/order/ method PUT
# {
#    "id_user":2,
#    "book_id":6000,
#    "count":1
# }
#http://127.0.0.1:8000/api/v1/order/?id_user=1 method GET
#http://127.0.0.1:8000/api/v1/order/?id_user=1&id_sale=1 method delete
