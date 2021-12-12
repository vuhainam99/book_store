
from django.shortcuts import render



def index(request):
    
    context = {'latest_question_list': 'latest_question_list'}
    return render(request, 'landingpage/index.html', context)