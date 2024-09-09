from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')

def bamee(request):
    return render(request, 'bamee.html')

def baknut(request):
    return render(request, 'buknut.html')

def hoykom(request):
    return render(request, 'hoykom.html')

def creater(request):
    return render(request, 'creater.html')

def cal(request):
    return render(request,"calory.html")