from django.shortcuts import render
from django.http import  HttpResponse

def Suprise(request):
    return render(request,'HappyBirtday.html')
