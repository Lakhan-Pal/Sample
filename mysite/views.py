from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"home.html")
def aboutUs(request):
    #return HttpResponse('Welcome to my site')
    return render(request,"about.html")