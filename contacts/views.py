from django.shortcuts import render, redirect
from django.contrib import messages, redirects
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Your request has been submitted, thank you for sharing your opinion')
        
    return render(request, 'contacts/contact.html')