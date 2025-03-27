from django.shortcuts import render, HttpResponse
import os

def index(request):
    return render(request, 'index.html')

def workers(request):
    return render(request, 'workers.html')
def unskilled(request):
    return render(request, 'unskilled.html')
def skilled(request):
    return render(request, 'skilled.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Ensure the directory exists
        directory = r"C:\Users\ninad\OneDrive\Desktop\Workers-Helpline\workers_helpline\contact-messages"
        os.makedirs(directory, exist_ok=True)
        
        # Save data to a text file
        file_path = os.path.join(directory, 'contact_messages.txt')
        with open(file_path, 'a') as file:
            file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n{'-'*40}\n")
        
        return HttpResponse("Your message has been submitted successfully!")

    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')