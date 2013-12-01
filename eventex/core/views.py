# coding: utf-8

# from django.http import HttpResponse # Use with method 1 and 2
# from django.template import loader, Context # Use with method 2
# from django.shortcuts import render_to_response # Use with method 3, 4 and 5
# from django.conf import settings # Use with method 4
# from django.template import RequestContext # Use with method 5
from django.shortcuts import render # Use with method 6


# View is Callable
# Callable - Object executable (Thunder call?)

# Function by default is Callable
# Method 5
def home(request):
    return render(request, 'index.html')

'''
# Method 5
def home(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)

# Method 4
def home(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('index.html', context)

# Method 3
def home(request):
    return render_to_response('index.html')

# Method 2
def home(request):
    t = loader.get_template('index.html')
    c = Context()

    content = t.render(c)

    return HttpResponse(content)

# Method 1
def home(request):
    return HttpResponse('EventeX - Plataforma de Eventos - Criada pela comunidade Python com Django!')
'''
