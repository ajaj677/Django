import re
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hellow, world. You are at codeZERO")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("hellow, world. You are at codeZERO about page")

def contact(request):
    return HttpResponse("hellow, world. You are at codeZERO contact page")
