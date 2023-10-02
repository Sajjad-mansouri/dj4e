from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request,'polls/index.html')
def owner(request):
	return HttpResponse("Hello, world. 77be07f3 is the polls index.")

def detail(request,question_id):
	return render(request,'polls/detail.html',context={'question_id':question_id})

def results(request,question_id):
	return render(request,'polls/results.html',context={'question_id':question_id})

def vote(request,question_id):
	return HttpResponse(f"Hello, world. 77be07f3 is the polls index.vot  :{question_id}")