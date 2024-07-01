from django.http import HttpResponse
from django.shortcuts import render


def hello_from_kuber(request):
    return HttpResponse("Hello from kuber!")
