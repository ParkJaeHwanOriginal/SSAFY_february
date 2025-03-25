from django.shortcuts import render
import random

# Create your views here.
def index(request) : 
    context = {
        'name' : 'Jane'
    }
    return render(request, 'index.html', context)

def dinner(request) : 
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'dinner.html', context)

def search(request) : 
    return render(request, 'search.html')

def throw(request) : 
    return render(request, 'throw.html')

def catch(request) : 
    print(request)                              # <WSGIRequest: GET '/catch/?message=sdf'>
    print(type(request))                        # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.GET)                          # <QueryDict: {'message': ['sdf']}>
    print(request.GET.get('message'))
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def detail(request, num) : 
    context = {
        'num' : num,
    }
    return render(request, 'detail.html', context)