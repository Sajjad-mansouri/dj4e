from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
	num=request.session.get('num',0)+1
	request.session['num']=num
	if num>4 :
		del request.session['num']
	resp=HttpResponse(f'dcbe0f23,view count:{num}')
	resp.set_cookie('dj4e_cookie', 'dcbe0f23', max_age=1000)
	return resp
