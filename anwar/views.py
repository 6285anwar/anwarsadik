from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'anwar.html')


#---------------------------------- WORKS ------------------------------------

def calculator(request):
    return render(request,'works/calculator.html')
def stopwatch(request):
    return render(request,'works/stopwatch.html')