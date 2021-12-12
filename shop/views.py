
from django.shortcuts import render
from api.models import *


def shop_view(request):
    pass
    context = {'latest_question_list': 'latest_question_list'}
    return render(request, 'shop/index-base.html', context)

def detail_view(request,id_book=None):
    book = Book.objects.get(id=id_book)
    context = {'book': book}
    return render(request, 'shop/detail-base.html', context)

def cart_now(request,id_book=None):
    book = Book.objects.get(id=id_book)
    context = {'book': book}
    return render(request, 'shop/cart-now.html', context)