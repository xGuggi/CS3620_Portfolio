from django.http import HttpResponse
from django.shortcuts import render
from .models import Hobbies
from .models import Portfolio
from django.template import loader


# Create your views here.
def home(request):
    template = loader.get_template('PortfolioDatabase/index.html')
    context = {
        'welcome_message': """Welcome to my Portfolio! In the dynamic landscape of technology, the pursuit of 
        knowledge in computer science has become an exhilarating journey. As a senior at Weber State University, 
        I have had the privilege of delving into the intricacies of this ever-evolving field."""
    }
    return render(request, 'PortfolioDatabase/index.html', context)


def hobbies(request):
    hobbies_list = Hobbies.objects.all()
    template = loader.get_template('PortfolioDatabase/hobbies.html')
    context = {
        'hobbies_list': hobbies_list,
    }
    return render(request, 'PortfolioDatabase/hobbies.html', context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    template = loader.get_template('PortfolioDatabase/portfolio.html')
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'PortfolioDatabase/portfolio.html', context)


def contact(request):
    template = loader.get_template('PortfolioDatabase/contact.html')
    context = {
        'contact_info': """Student Email: spencerguggisberg@mail.weber.edu"""
    }
    return render(request, 'PortfolioDatabase/contact.html', context)


def detail_hobbies(request, hobbies_id):
    hobbies = Hobbies.objects.get(pk=hobbies_id)
    context = {
        'hobbies': hobbies
    }
    return render(request, 'PortfolioDatabase/detail_hobbies.html', context)

def detail_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'PortfolioDatabase/detail_portfolio.html', context)
