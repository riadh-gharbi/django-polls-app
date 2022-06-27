from django.shortcuts import render

# Create your views here.
# from the django docs
from django.http import HttpResponse
# Simple view that returns an http Response
# We need to map it to a URL , for this we need a URLconf


def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")

