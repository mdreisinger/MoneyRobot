from django.http import HttpResponse
from django.template import loader
#from django.shortcuts import render

from .models import expenses


def index(request):
	expenses_list = expenses.objects.order_by('id')
	
	template = loader.get_template('index.html')
	
	context = {
             'expenses_list': expenses_list,
        }
    
	return HttpResponse(template.render(context, request))
	
	#context = {'user_list': user_list}
	#return render(request, 'index.html', context)