from django.http import HttpResponse
from django.shortcuts import render
from .models import Hobbies
from .models import Portfolio


# Create your views here.
def Home(request):
    return HttpResponse("Welcome to my Portfolio! In the dynamic landscape of technology, the pursuit of knowledge in "
                        "computer science has become an exhilarating journey. As a senior at Weber State University, "
                        "I have had the privilege of delving into the intricacies of this ever-evolving field.  ")


def Hobbies(request):
    hobbies_list = Hobbies.objects.all()
    return HttpResponse(hobbies_list)


def Portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def Contact(request):
    return HttpResponse("Student Email: spencerguggisberg@mail.weber.edu")
