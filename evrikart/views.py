from django.shortcuts import render


def check_mail_temp(request):
    return render(request, 'mail/regenerate_verfication_link.html')