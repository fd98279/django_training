from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    return render(request, "hello.html")

def post_test(request):
    return render(request, "hello_post.html")

def add(request):
    return render(request, "result.html", {'result': request.GET['num1'] + request.GET['num2']})

def add_post(request):
    return render(request, "result.html", {'result': request.POST['num1'] + request.POST['num2']})

def static_test(request):
    dests = models.Destination.objects.all()
    return render(request, "travello_index.html", { 'dests': dests})