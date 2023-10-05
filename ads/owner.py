from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(ListView):
	pass

class OwnerDetailView(DetailView):
	pass

class OwnerCreateView(LoginRequiredMixin,CreateView):
	
	def form_valid(self,form):
		object=form.save(commit=False)
		object.owner=self.request.user
		object.save()
		return super().form_valid(form)

class OwnerUpdateView(LoginRequiredMixin,UpdateView):
	
	def get_queryset(self):
		qs=super().get_queryset()
		qs=qs.filter(owner=self.request.user)
		return qs

class OwnerDeleteView(LoginRequiredMixin,DeleteView):
	
	def get_queryset(self):
		qs=super().get_queryset()
		qs=qs.filter(owner=self.request.user)
		return qs
