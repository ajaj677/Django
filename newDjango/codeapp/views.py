from django.shortcuts import render

# Create your views here.

def code_arena(request):
    return render (request, 'codeapp/all_codeapp.html')