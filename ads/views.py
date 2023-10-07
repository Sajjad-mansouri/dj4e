from django.shortcuts import render,get_object_or_404,redirect
from  .owner import (OwnerListView,
						OwnerDetailView,
						OwnerCreateView,
						OwnerUpdateView,
						OwnerDeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Ad,Comment,Fav
from .forms import AdForm,CommentForm

class AdListView(OwnerListView):
	model=Ad
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*args,**kwargs)
		favorites=list()
		if self.request.user.is_authenticated:
			rows=self.request.user.favorite_ads.values('id')
			favorites=[row['id'] for row in rows]
		context['favorites']=favorites
		return context
class AdDetailView(OwnerDetailView):
	model=Ad

	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*args,**kwargs)

		context['comment_form']=CommentForm()
		context['comments']=Comment.objects.filter(ad=self.object).order_by('-updated')
		context['favorites']=favorites
		return context

class AdCreateView(OwnerCreateView):
	model=Ad
	form_class=AdForm

class AdUpdateView(OwnerUpdateView):
	model=Ad
	form_class=AdForm

class AdDeleteView(OwnerDeleteView):
	model=Ad



def stream_file(request,pk):
	obj=Ad.objects.get(id=pk)
	response=HttpResponse()
	response['Content-Type']=obj.content_type
	response['Content-Length']=len(obj.picture)
	response.write(obj.picture)
	return response


class CommentCreateView(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
			pk=self.kwargs.get('pk')
			ad=get_object_or_404(Ad,id=pk)
			owner=request.user
			comment=Comment.objects.create(text=request.POST['comment'],ad=ad,owner=owner)
			return redirect(reverse('ads:ad_detail',args=[pk]))



class CommentDeleteView(OwnerDeleteView):
	model=Comment
	template_name = "ads/comment_delete.html"

	def get_success_url(self):
		forum = self.object.ad
		print(self.object)
		return reverse('ads:ad_detail', args=[forum.id])

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(View):
	def post(self,request,*args,**kwargs):
		pk=self.kwargs.get('pk')
		ad=get_object_or_404(Ad,id=pk)
		fav=Fav(ad=ad,user=request.user)
		try:
			fav.save()
		except Exception as e:
			print(e)

		return HttpResponse()
@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(View):
	def post(self,request,*args,**kwargs):
		pk=self.kwargs.get('pk')
		ad=get_object_or_404(Ad,id=pk)
		try:
			Fav.objects.get(ad=ad,user=request.user).delete()
		except Exception as e:
			print(e)

		return HttpResponse()