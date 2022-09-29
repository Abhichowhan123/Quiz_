from django.shortcuts import render

# Create your views here.
from unicodedata import category
from django.shortcuts import render
from.models import *
from django.http import JsonResponse
# Create your views here.


def home(request):
    courses  =Course.objects.all()
    context =  {'courses':courses}
    return render(request,'index.html',context)

def quiz(request,id):
    context = {'id':id}
    return render(request,'quiz.html',context)

def api_question(request,id):
    R_questions = Question.objects.filter(course =id)
    questions = []
    for i in R_questions:
        question = {}
        question['question'] = i.question
        question['ans'] = i.ans

        options = []
        options.append(i.option_1)
        options.append(i.option_2)
        options.append(i.option_3)
        options.append(i.option_4)

        question['options']  =options

        questions.append(question)

    return JsonResponse(questions,safe = False)    