from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView,DetailView,ListView
from .models import Choice, Question

class IndexView(ListView):
	model=Question
	template_name='polls/index.html'
	
def owner(request):
	return render(request,'polls/owner.html')

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST["choice"])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(
			request,
			"polls/detail.html",
			{
				"question": question,
				"error_message": "You didn't select a choice.",
			},
		)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

class ResultsView(DetailView):
	model=Question
	context_object_name='question'
	template_name='polls/results.html'
class DetailView(DetailView):
	model = Question
	context_object_name='question'
	template_name = "polls/detail.html"
