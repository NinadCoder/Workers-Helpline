from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def workers(request):
    return render(request, 'workers.html')
def unskilled(request):
    return render(request, 'unskilled.html')
def skilled(request):
    return render(request, 'skilled.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')