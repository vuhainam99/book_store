
from django.shortcuts import render



def login_view(request):
    
    context = {'latest_question_list': 'latest_question_list'}
    return render(request, 'authen/login.html', context)



def sigup_view(request):
    
    context = {'latest_question_list': 'latest_question_list'}
    return render(request, 'authen/sigup.html', context)