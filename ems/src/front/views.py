from django.conf import settings

from django.shortcuts import render 

def home(request):

	template= "front_templates/home.html"
	context={
	}
	return render(request, template, context)
	
def landing(request):
	template= "front_templates/landinghome.html"
	context={
	}
	return render(request, template, context)
def about(request):
	template= "front_templates/about.html"
	context={
	}
	return render(request, template, context)
def sidebar(request):
	template= "side_templates/sidebar.html"
	context={
	}
	return render(request, template, context)


