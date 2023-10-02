from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 5ef19f54 is the polls index.")