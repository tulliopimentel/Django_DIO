from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hello(request):
    return HttpResponse('Hello World')