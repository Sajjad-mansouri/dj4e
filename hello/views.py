from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
	num=request.session.get('num',0)+1
	request.session['num']=num
	if num>4 :
		del request.session['num']
	return HttpResponse(f'visits:{num}')
