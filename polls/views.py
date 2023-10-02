from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello, world. 5ef19f54 is the polls index.")

def owner(request):
	return HttpResponse("Hello, world. 77be07f3 is the polls index.")

def detail(request,question_id):
	return HttpResponse(f"Hello, world. 77be07f3 is the polls index. question:{question_id}")

def results(request,question_id):
	return HttpResponse(f"Hello, world. 77be07f3 is the polls index.qusetion results:{question_id}")

def vote(request,question_id):
	return HttpResponse(f"Hello, world. 77be07f3 is the polls index.vot  :{question_id}")