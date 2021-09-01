from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hello(request):
    return HttpResponse('Hello World')


def Soma(request, n1, n2):
    total = n1 + n2
    return HttpResponse("A soma de {} + {} é {}".format(n1, n2, total))

def Sub(request, n1, n2):
    total = n1 - n2
    return HttpResponse("A subtração de {} - {} é {}".format(n1, n2, total))

def Div(request, n1, n2):
    total = n1 / n2
    return HttpResponse("A divisão de {} / {} é {}".format(n1, n2, total))

def Mult(request, n1, n2):
    total = n1 * n2
    return HttpResponse("A multiplicação de {} * {} é {}".format(n1, n2, total))