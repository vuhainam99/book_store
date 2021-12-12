from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.renderers import JSONRenderer
import json
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication, 
    TokenAuthentication
)
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
import os
from api.cron import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from api.callAPI import callAPI_transportorder
from .models import * #import model vao day 
from .serializers import * #import serializers vao day 
from api.Book_recommendation_model_2 import * #import
from datetime import datetime,timedelta
from django.utils.crypto import get_random_string
import logging
import random
# Get an instance of a logger
logger = logging.getLogger(__name__)
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages

        
# 'mau api_view'
# @api_view(['get','post','delete','put']) 
# # @authentication_classes([SessionAuthentication, TokenAuthentication])
# # @permission_classes([IsAuthenticated])
# def API_Config(request):
#     try:
#         if request.method == 'POST':
#             method_id = request.query_params.get('method_id',None)
#             if method_id == "users":
#                 books = pandas.read_csv("./csv_sach/users.csv",engine="python").to_dict()
#                 leng = len(books['userId'])
#                 for i in range(leng):
                    
                    
#                     users = Users(first_name=books['first_name'][i] ,last_name= books['last_name'][i],phone= books['phone'][i],email= books['email'][i],password= books['password'][i],ratingCount= books['ratingCount'][i])
#                     users.save()
#             elif method_id == 'ratings' :
#                 books = pandas.read_csv("./csv_sach/ratings.csv",engine="python").to_dict()
#                 leng = len(books['user_id'])
                
#                 for i in range(leng):
                    
#                     book_id = Book.objects.get(id=int(books['book_id'][i])+2201)
#                     user_id = Users.objects.get(id=int(books['user_id'][i]))
#                     rating = User_rating(user = user_id ,book_id = book_id,rating = books['rating'][i])
#                     rating.save()
                    
#             return Response({'status': 201,'data':""})
#         if request.method == 'GET':
# books = pandas.read_csv("./csv_sach/books.csv",engine="python").to_dict()
# book_obj_ls = Book.objects.filter(book_authors=books['authors'][1],book_title=books['original_title'][1])
# print(len(book_obj_ls))
# book_obj_ls = Book.objects.all()
# for i in book_obj_ls:
#     try:
#         book_data_obj = Book_Data(book_id =i,authors=i.book_authors,original_title=i.book_title,image_url=i.image_url)
#         book_data_obj.save()
#     except Exception as ex:
#         print(i.id)
#         i.delete()
            
#             return Response({'status': 201,'data':'okok'})
#         if request.method == 'PUT':
            # books = pandas.read_csv("./csv_sach/book_data.csv",engine="python").to_dict()
            # leng = len(books['book_id'])

            # for i in range(leng):
            #     if isinstance(books['book_pages'][i],float) or isinstance(books['book_desc'][i],float) or isinstance(books['book_edition'][i],float):
            #         continue
            #     else:
            #         book_pages = books['book_pages'][i]
            #     try:
            #         book = Book(
            #             book_authors=books['book_authors'][i],
            #             book_desc=books['book_desc'][i],
            #             book_edition =books['book_edition'][i],
            #             book_format =books['book_format'][i],
            #             book_isbn = books['book_isbn'][i],
            #             book_pages = book_pages,book_rating = books['book_rating'][i],
            #             book_rating_count = books['book_rating_count'][i],
            #             book_review_count = books['book_review_count'][i],
            #             book_title = books['book_title'][i],
            #             genres = books['genres'][i],
            #             image_url = books['image_url'][i],
            #             book_price = books['book_price'][i]
            #         )
            #         book.save()
            #     except:
            #         continue
#             return Response({'status': 201,'data':''})
#         if request.method == 'DELETE':
#             books = pandas.read_csv("./csv_sach/books.csv",engine="python").to_dict()
#             leng = len(books['book_id'])
#             print(books['image_url'][1])
#             # for i in range(leng):
#             #     book_data_obj_ls = Book_Data.objects.filter(image_url=books['image_url'][1])
#             #     print(len(book_data_obj_ls))

#             return Response({'status': 201,'data':''})
#     except Exception as ex:
#         error = str(ex)
#         logger.warning(str(request.data) + " - " + error)
#         return Response({'status': 401, 'error': str(ex),'data': {}})

# 'dang nhap '
@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def API_login(request):
    try:
        if request.method == 'POST': # dang nhap 
            data = request.data
            username = data['email']
            password = data['password']
            print(username)
            print(password)
            user_obj_ls = Users.objects.filter(email=username, password=password)
            if len(user_obj_ls) != 0 :
                dic = {
                    'username':username,
                    'id':user_obj_ls[0].id
                }
                
                return Response({'status': 201,'data':dic})
            else:
                return Response({'status': 401,'data':0})
        if request.method == 'PUT': # dang ky 
            data = request.data
            first_name = data['first_name']
            last_name = data['last_name']
            phone = data['phone']
            email = data['email']
            password = data['password']
            user_obj_check = Users.objects.filter(email=email)
            if len(user_obj_check) == 0:
                user_obj = Users(first_name=first_name, last_name=last_name,phone=phone,email=email,username='',password=password)
                user_obj.save()
                order_book = Order(user=user_obj,order_info="",order_code=phone)
                order_book.save()
            else:
                return Response({'status': 401,'data':'da ton tai'})
            return Response({'status': 201,'data':'create ss'})
        if request.method == 'GET':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            pass
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})

# 'dang nhap '
@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def Book_API(request):
    try:
        if request.method == 'POST':
            data = request.data
            return Response({'status': 201,'data':""})
        if request.method == 'GET': # lay danh sach san pham moi nhat random 36 quyen trong 360 quyen moi nhat
            Book_obj = Book.objects.all().order_by("-id")
            serializers = BookSerializer(Book_obj[:360],many=True)
            return Response({'status': 201,'data':random.sample(serializers.data, 36)})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            pass
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})



# 'dang nhap '
@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def Book_details_API(request):
    try:
        if request.method == 'POST':
            pass
            return Response({'status': 201,'data':""})
        if request.method == 'GET': # tim kiem sach + lay thong tin details
            dic_params = {}
            id_book = request.query_params.get('id_book',None) 
            dic_params['book_title__contains'] = request.query_params.get('book_title',None)          
            genres_vi   = request.query_params.get('genres',None)
            if genres_vi is not None:
                geres_obj = Genres.objects.get(genres_vi=genres_vi)
                genres_eg = geres_obj.genres_eg
                dic_params['genres__contains'] = genres_eg   
                   
            # tim nhung params ko None tao thanh dic arguments
            arguments = {}
            for k, v in dic_params.items():
                if v:
                    arguments[k] = v 
            if id_book is None:
                Book_obj = Book.objects.filter(**arguments)
            else:
                Book_obj = Book.objects.filter(id=id_book)
            
            serializers = BookSerializer(Book_obj[:80],many=True)
            return Response({'status': 201,'data':serializers.data})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            pass
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})

# 'dang nhap '
# @api_view(['get','post','delete','put']) 
# # @authentication_classes([SessionAuthentication, TokenAuthentication])
# # @permission_classes([IsAuthenticated])
# def Book_recommender_API(request):
#     try:
#         if request.method == 'GET': # lay danh sach book recommender
#             id_user = request.query_params.get('id_user',None) 
#             ratings = pandas.read_csv("./csv_sach/ratings1.csv",engine="python")
#             d = (ratings.groupby('user_id')['book_id','rating'].apply(lambda x: dict(x.values)).to_dict())
#             print(len(d))
#             userId= int(id_user)
#             try:
#                 rec_books = get_recommendations(d, userId)
#                 ls_book = []
#                 if len(ls_book) != 0:
#                     for i in rec_books:
#                         id_book = i[1]
#                         book = Book.objects.get(id=id_book)
#                         serializers = BookSerializer(book)
#                         ls_book.append(serializers.data)
#                 else:
#                     book_obj_ls = Book.objects.all()
#                     serializers = BookSerializer(book_obj_ls[:8],many=True)
#                     ls_book = serializers.data
#             except:
#                 book_obj_ls = Book.objects.all()
#                 serializers = BookSerializer(book_obj_ls[:8],many=True)
#                 ls_book = serializers.data
#             return Response({'status': 201,'data':random.sample(ls_book, 4)})
#         if request.method == 'PUT': # dong bo database voi file rating1.csv
#             user_ratings_obj_ls = User_rating.objects.all()
#             ls_user_id = []
#             ls_book_id = []
#             ls_rating = []
#             for i in user_ratings_obj_ls:
#                 ls_user_id.append(i.user.id)
#                 ls_book_id.append(i.book_id.id)
#                 ls_rating.append(i.rating)
#             dic = {}
#             dic['user_id'] = ls_user_id
#             dic['book_id'] = ls_book_id
#             dic['rating'] = ls_rating
#             df = pandas.DataFrame(dic)
#             df.to_csv("./csv_sach/ratings1.csv", sep=',',index=False)
#             return Response({'status': 201,'data':dic})
#         if request.method == 'POST':
#             pass
#             return Response({'status': 201,'data':''})
#         if request.method == 'DELETE':
#             pass
#             return Response({'status': 201,'data':''})
#     except Exception as ex:
#         error = str(ex)
#         logger.warning(str(request.data) + " - " + error)
#         return Response({'status': 401, 'error': str(ex),'data': {}})


# 'dang nhap '
@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def List_gerses_book(request):
    try:
        if request.method == 'GET': # lay danh sach danh muc sach
            Genres_ls = Genres.objects.all()
            ls = []
            for i in Genres_ls:
                ls.append(i.genres_vi)
            return Response({'status': 201,'data':random.sample(ls, 8)})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':dic})
        if request.method == 'POST':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            pass
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})

# 'dang nhap '
@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def Oder_book_API(request):
    try:
        if request.method == 'GET': # lay danh sach don hang theo user
            id_user = request.query_params.get('id_user',None) 
            user_obj = Users.objects.get(id=id_user)
            order_obj_check = Order.objects.filter(user=user_obj)
            ls = []
            if len(order_obj_check) != 0:
                Book_Sales_His_obj = Book_Sales_His.objects.filter(order=order_obj_check[0],status=0)
                for i in Book_Sales_His_obj:
                    serializers = BookSerializer(i.book_id)
                    dic = {
                        "id":i.id,
                        "book":serializers.data,
                        "count":i.count
                    }
                    ls.append(dic)
            return Response({'status': 201,'data':ls})
        if request.method == 'POST': # tao gio hang theo user
            data = request.data
            user_id = data['id_user']
            user_obj = Users.objects.get(id=user_id)
            order_obj_check = Order.objects.filter(user=user_obj)
            if len(order_obj_check) == 0:
                order_book = Order(user=user_obj,order_info="",order_code=user_obj.phone)
                order_book.save()
            return Response({'status': 201,'data':''})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':'save ok'})
        if request.method == 'DELETE': # xac nhan mua hang va gui mail
            # id_sale = request.query_params.get('id_sale',None) 
            id_user = request.query_params.get('id_user',None) 


            user_obj = Users.objects.get(id=id_user)
            order_obj = Order.objects.filter(user=user_obj)
            Book_Sales_His_obj = Book_Sales_His.objects.filter(order=order_obj[0],status=0)
            ls = 'Bạn vừa đặt mua thành công đơn hàng: \n '
            for i in Book_Sales_His_obj:
                string = "-Sách " + i.book_id.book_title + "-số lượng {} \n".format(i.count)
                ls += string
            #gui mail
            subject = "Thông tin đơn hàng"
            message = ls

            sender = 'dangphongrecommendbook'
            recipient = [user_obj.email]
            try:
                print(1)
                send_mail(subject, message, sender, recipient, fail_silently=True)
                print(2)
            except BadHeaderError:
                print(0)
            Book_Sales_His_obj.update(status=1)
            
            return Response({'status': 201,'data':'xac nhan tao don hang'})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})


# 'dang nhap '
@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def add_cart(request): # them san pham vao gio hang
    try:
        if request.method == 'GET':
            user_id = request.query_params.get('id_user',None) 
            book_id = request.query_params.get('book_id',None) 

            user_obj = Users.objects.get(id=user_id)
            book_obj = Book.objects.get(id=book_id)
            order_obj_check = Order.objects.filter(user=user_obj)
            Book_Sales_His_obj_check = Book_Sales_His.objects.filter(order=order_obj_check[0],book_id=book_obj,status=0)
            if len(Book_Sales_His_obj_check) == 0:
                Book_Sales_His_obj = Book_Sales_His(order=order_obj_check[0],book_id=book_obj,count=1)
                Book_Sales_His_obj.save()
            return Response({'status': 201,'data':ls})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':dic})
        if request.method == 'POST':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            pass
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})

# from django.core.mail import send_mail,BadHeaderError
# 'dang nhap '
@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def rating_api(request): # them danh gia sach
    try:
        if request.method == 'GET':
            user_id = request.query_params.get('user_id',None) 
            id_book = request.query_params.get('id_book',None) 
            rating = request.query_params.get('rating',None) 
            # data = request.data
            # user_id = data['user_id']
            # id_book = data['id_book']
            # rating = data['rating']
            user_obj = Users.objects.get(id=user_id)
            book_obj = Book.objects.get(id=id_book)
            rating_obj_ls_ckeck = User_rating.objects.filter(user=user_id,book_id=id_book)
            
            if len(rating_obj_ls_ckeck) == 0:
                rating_obj = User_rating(user=user_obj,book_id=book_obj,rating=rating)
                rating_obj.save()
            else:
                rating_obj_ls_ckeck.update(rating=rating)
            return Response({'status': 201,'data':""})
        if request.method == 'POST':
            pass
            return Response({'status': 201,'data':ls})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            pass
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})

@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def rating_show(request): # xem danh sach sach da duoc danh gia theo user
    try:
        if request.method == 'GET':
            user_id = request.query_params.get('user_id',None)
            rating_obj_ls_ckeck = User_rating.objects.filter(user=user_id)
            ls = []
            for i in rating_obj_ls_ckeck:
                serializers = BookSerializer(i.book_id)
                dic = {
                    "book": serializers.data,
                    "rating": i.rating
                }
                ls.append(dic)
            return Response({'status': 201,'data':ls})
        if request.method == 'POST':
            pass
            return Response({'status': 201,'data':ls})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            pass
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})

@api_view(['get','post','delete','put']) 
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def send_mail_buynow(request): # xem danh sach sach da duoc danh gia theo user
    try:
        if request.method == 'GET':
            pass
            return Response({'status': 201,'data':ls})
        if request.method == 'POST':
            pass
            return Response({'status': 201,'data':ls})
        if request.method == 'PUT':
            pass
            return Response({'status': 201,'data':''})
        if request.method == 'DELETE':
            id_user = request.query_params.get('id_user',None)
            
            id_book = request.query_params.get('id_book',None)
            
            user_obj = Users.objects.get(id=id_user)
            
            book_obj = Book.objects.get(id=id_book)
            ls = 'Bạn vừa đặt mua thành công đơn hàng: \n '
            
            string = "-Sách " + book_obj.book_title + "-số lượng {} \n".format(1)
            ls += string
            #gui mail
            subject = "Thông tin đơn hàng"
            message = ls
            sender = 'dangphongrecommendbook'
            recipient = [user_obj.email]
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)

            except BadHeaderError:
                print(0)
            return Response({'status': 201,'data':''})
    except Exception as ex:
        error = str(ex)
        logger.warning(str(request.data) + " - " + error)
        return Response({'status': 401, 'error': str(ex),'data': {}})
