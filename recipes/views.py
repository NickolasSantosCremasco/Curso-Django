from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Bom dia')

def contato(request):
    return HttpResponse('tabem')

def sobre(request):
    return HttpResponse('eae')