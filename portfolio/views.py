from django.shortcuts import render
from .models import Portfolio


def portfolio_view(request):
    """
    Return a response for the Portfolio page.

    Args:
        request (HttpRequest): A GET request.

    Returns:
        HttpResponse: Contains the Portfolio page.
    """
    portfolio = Portfolio.objects.first()
    context = {"portfolio": portfolio}
    return render(request, "portfolio/portfolio.html", context)
