from django.shortcuts import render

# Create your views here.
def workers(request):
    return render(request, 'workers.html')
def unskilled(request):
    return render(request, 'unskilled.html')
def skilled(request):
    return render(request, 'skilled.html')
def hire(request):
    return render(request, 'hire.html')