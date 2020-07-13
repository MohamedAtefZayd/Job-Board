from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from project import settings


def send_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],)
    return render(request,'contact/contact.html')