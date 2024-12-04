from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about(request):
    if request.method == 'GET':
        return HttpResponse("Привет, меня зовут Даня, мне 17 лет!")
    
def about_pet(request):
    if request.method == 'GET':
        return HttpResponse("У меня есть собака по кличке Нора. Ее порода - Малинуа")
    
    
def system_time(request):
    if request.method == 'GET':
        current_time = datetime.now()
        return HttpResponse(f"Текущее время: {current_time}")