from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Contact




def HomePageView(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create( name = name, email = email, subject = subject, message = message )

        successful = messages.success( request, 'Your message has been successfully sent!')

        

    return render(request, 'index.html' )




# class HomePageView(TemplateView):

#     template_name = 'index.html'

#     def post(self, request):
#         if request.method == "POST":
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             subject = request.POST.get('subject')
#             message = request.POST.get('message')

#             Contact.objects.create( name = 'name', email = 'email', subject = 'subject', message = 'message')

#             successful = messages.success( request, 'Your message has been successfully sent!')

#         return HomePageView