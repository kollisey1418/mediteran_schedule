from django.shortcuts import render

def index(request):
    return render(request, 'schedule/schedule.html')
def home(request):
    return render(request, 'schedule/home.html')  # Указываем на шаблон 'home.html'
def sveti_stefan(request):
    return render(request, 'schedule/budva-sveti-stefan-budva.html')

def petrovac(request):
    return render(request, 'schedule/budva-petrovac-budva.html')

def lastva(request):
    return render(request, 'schedule/budva-lastva-budva.html')