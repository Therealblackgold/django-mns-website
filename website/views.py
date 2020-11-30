from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def success(request):
    return render(request, 'about.html', {})
    

def contact(request):
    if request.method == "POST":
    
        # DO THIS
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']


        # SEND EMAIL
        send_mail(
            message_name,
            message,
            message_email,
            ['mnsinnovations@gmail.com'], # TO THIS EMAIL ADDRESS
            fail_silently=False,
        )
        return render(request,'success.html',{'message_name':message_name})
    else: 
        return render(request, 'contact.html', {})