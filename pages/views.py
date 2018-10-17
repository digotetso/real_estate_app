from django.shortcuts import render
from django.http import HttpResponse

def index (requests):
    return render(requests, 'pages/index.html')

def about (requests):
    return render(requests, 'pages/about.html')
