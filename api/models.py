from re import T
from django.db import models
import json
import datetime
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE
from django.utils.crypto import get_random_string
from django.db import IntegrityError
# Create your models here.

class Users(models.Model):
    first_name         = models.CharField(max_length=50)
    last_name          = models.CharField(max_length=50)
    phone              = models.CharField(max_length=15)
    username           = models.CharField(max_length=50,null=True)
    email              = models.EmailField(max_length=50)
    password           = models.CharField(max_length=50)
    ratingCount        = models.IntegerField(default=0)
    created_date       = models.DateTimeField(auto_now_add=True, verbose_name=("created date"))

class Book(models.Model):
    book_authors = models.CharField(max_length=250)
    book_desc = models.CharField(max_length=10000)
    book_edition = models.CharField(max_length=250)
    book_format = models.CharField(max_length=250)
    book_isbn = models.CharField(max_length=250)
    book_pages = models.IntegerField(default=0)
    book_rating = models.FloatField(default=0)
    book_rating_count = models.IntegerField(default=0)
    book_review_count = models.IntegerField(default=0)
    book_title = models.CharField(max_length=250)
    genres = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250)
    book_price = models.IntegerField(default=0)

class Book_info(models.Model):
    book = models.ForeignKey(Book,related_name="book_if",on_delete=CASCADE)
    quantity_in_stock = models.IntegerField(default=0)
    source = models.CharField(max_length=50)

class User_rating(models.Model):
    user              = models.ForeignKey(Users,related_name="user_id",on_delete=CASCADE)
    book_id           = models.ForeignKey(Book,related_name="book_id",on_delete=CASCADE)
    rating            = models.SmallIntegerField(default=0)
    created_date      = models.DateTimeField(auto_now_add=True, verbose_name=("created date"))

class User_To_read(models.Model):
    user              = models.ForeignKey(Users,related_name="id_user",on_delete=CASCADE)
    book_id           = models.ForeignKey(Book,related_name="id_book",on_delete=CASCADE)
    created_date      = models.DateTimeField(auto_now_add=True, verbose_name=("created date"))

class Book_Data(models.Model):
    book_id = models.ForeignKey(Book,related_name="book",on_delete=CASCADE)
    goodreads_book_id = models.IntegerField(default=0)
    best_book_id = models.IntegerField(default=0)
    work_id = models.IntegerField(default=0)
    books_count = models.IntegerField(default=0)
    isbn = models.IntegerField(default=0)
    isbn13 = models.CharField(max_length=50)
    authors = models.CharField(max_length=250)
    original_publication_year = models.FloatField(default=0)
    original_title = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    language_code = models.CharField(max_length=10)
    average_rating = models.FloatField(default=0)
    ratings_count = models.IntegerField(default=0)
    work_ratings_count = models.IntegerField(default=0)
    work_text_reviews_count = models.IntegerField(default=0)
    ratings_1 = models.IntegerField(default=0)
    ratings_2 = models.IntegerField(default=0)
    ratings_3 = models.IntegerField(default=0)
    ratings_4 = models.IntegerField(default=0)
    ratings_5 = models.IntegerField(default=0)
    image_url = models.CharField(max_length=100)
    small_image_url = models.CharField(max_length=100)

class Order(models.Model):
    user = models.ForeignKey(Users,related_name="user_sale",on_delete=CASCADE)
    order_code = models.CharField(max_length=30)
    order_info = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=("created date"))



class Book_Sales_His(models.Model):
    order        = models.ForeignKey(Order,related_name="order_id",on_delete=CASCADE)
    book_id      = models.ForeignKey(Book,related_name="book_sale",on_delete=CASCADE)
    count        = models.IntegerField(default=0)
    status       = models.SmallIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=("created date"))


class Genres(models.Model):
    genres_vi = models.CharField(max_length=100)
    genres_eg = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=("created date"))
