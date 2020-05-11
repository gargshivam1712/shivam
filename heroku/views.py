from django.shortcuts import render,redirect
from django.http import HttpResponse
import smtplib
import random
num=111111

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def submitlogin(request):
    if(request.method=="POST"):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
    return HttpResponse("Submit Successfully...")
