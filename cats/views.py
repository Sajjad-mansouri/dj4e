from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Cat,Breed


class CatList(LoginRequiredMixin,ListView):
	model=Cat
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*args,**kwargs)
		context['breed_count']=Breed.objects.count()
		return context

class CatCreate(LoginRequiredMixin,CreateView):
	model=Cat
	fields='__all__'
	success_url=reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin,UpdateView):
	model=Cat
	fields='__all__'
	success_url=reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin,DeleteView):
	model=Cat
	success_url=reverse_lazy('cats:all')


class BreedList(LoginRequiredMixin,ListView):
	model=Breed


class BreedCreate(LoginRequiredMixin,CreateView):
	model=Breed
	fields='__all__'
	success_url=reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin,UpdateView):
	model=Breed
	fields='__all__'
	success_url=reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin,DeleteView):
	model=Breed
	success_url=reverse_lazy('cats:all')
