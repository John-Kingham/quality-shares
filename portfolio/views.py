from django.shortcuts import render
from .models import Portfolio


def portfolio(request):
    portfolio = Portfolio.objects.first()
    context = {"portfolio": portfolio}
    return render(request, "portfolio/portfolio.html", context)
