from django.http import HttpResponse
from django.shortcuts import render
from importlib_metadata import re

# Create your views here.
#land page
def home (request):
    return render(request, 'website/index.html')
#compiler page
def vs (request):
    return render (request, "COMPILER/index.html")







