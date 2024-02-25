from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, PortfolioForm
from .models import Hobbies
from .models import Portfolio
from django.template import loader
from django.contrib.auth.decorators import login_required


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
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/PortfolioDatabase/')

    return render(request, 'PortfolioDatabase/contact-form.html', {'form': form})


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


@login_required
def portfolio_add(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/PortfolioDatabase/portfolio')

    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form})


@login_required
def portfolio_update(request, id):
    portfolio = Portfolio.objects.get(id=id)
    form = PortfolioForm(request.POST or None, instance=portfolio)

    if form.is_valid():
        form.save()
        return redirect('/PortfolioDatabase/portfolio')

    return render(request, 'PortfolioDatabase/portfolio-form.html', {'form': form, 'portfolio': portfolio})


@login_required
def portfolio_delete(request, id):
    portfolio = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        portfolio.delete()
        return redirect('/PortfolioDatabase/portfolio')

    return render(request, 'PortfolioDatabase/portfolio-delete.html', {'portfolio': portfolio})
