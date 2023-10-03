from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Auto,Make
from .forms import AutoForm,MakeForm


class MainView(LoginRequiredMixin,ListView):
	model=Auto
	template_name='autos/auto_list.html'
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*args,**kwargs)
		context['make_count']=Make.objects.count()
		return context

class AutoCreate(LoginRequiredMixin,CreateView):
	model=Auto
	form_class=AutoForm
	success_url=reverse_lazy('autos:all')
	template_name='autos/auto_form.html'

class AutoUpdate(LoginRequiredMixin,UpdateView):
	model=Auto
	form_class=AutoForm
	success_url=reverse_lazy('autos:all')
	template_name='autos/auto_form.html'

class AutoDelete(LoginRequiredMixin,DeleteView):
	model=Auto
	success_url=reverse_lazy('autos:all')
	template_name='autos/auto_delete_confirm.html'

class MakeView(LoginRequiredMixin,ListView):
	model=Make
	template_name='autos/make_list.html'

class MakeCreate(LoginRequiredMixin,CreateView):
	model=Make
	form_class=MakeForm
	success_url=reverse_lazy('autos:all')
	template_name='autos/make_form.html'

class MakeUpdate(LoginRequiredMixin,UpdateView):
	model=Make
	form_class=MakeForm
	success_url=reverse_lazy('autos:all')
	template_name='autos/make_form.html'

class MakeDelete(LoginRequiredMixin,DeleteView):
	model=Make
	success_url=reverse_lazy('autos:all')
	template_name='autos/make_delete_confirm.html'