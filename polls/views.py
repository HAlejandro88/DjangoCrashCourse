from django.shortcuts import render

from .models import Question, Choise

# Get questions and diplay

def index(request):
    return render(request, 'polls/index.html')

# minuto36:11