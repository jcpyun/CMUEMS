from django.conf import settings

from django.shortcuts import render 

def home(request):

	template= "front_templates/home.html"
	context={
	}
	return render(request, template, context)