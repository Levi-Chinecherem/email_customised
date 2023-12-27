# email_app/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EmailForm
from django.conf import settings  # Add this import

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_info = form.save()
            send_custom_email(email_info)
            return redirect('success')  # You need to define a success URL in urls.py
    else:
        form = EmailForm()

    return render(request, 'index.html', {'form': form})

def send_custom_email(email_info):
    subject = f"Message from {email_info.company_name}"
    message = email_info.message_content
    from_email = settings.EMAIL_HOST_USER  # Use the configured email
    recipient_list = [email_info.to_email]

    send_mail(subject, message, from_email, recipient_list)

def success_view(request):
    return render(request, 'success.html')  

