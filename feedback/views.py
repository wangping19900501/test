from django.shortcuts import render, redirect
from .models import *
from .forms import FeedbackForm
# Create your views here.

def create(request):
	if request.method=='POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/feedback/list')
	else:
		form = FeedbackForm()

	return render(request, 'feedback.html', {'form':form})

def list(request):
	feedbacks = Feedback.objects.all()
	return render(request, 'feedbacklist.html', {'feedbacks': feedbacks})

def edit(request, id):
	fb = Feedback.objects.get(pk=id)
	if request.method=='POST':
		form = FeedbackForm(request.POST, instance=fb)
		if form.is_valid():
			form.save()
		return redirect('/feedback/list')
	else:
		form = FeedbackForm(instance=fb)

	return render(request, 'feedback.html', {'form': form})