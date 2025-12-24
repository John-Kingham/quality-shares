from django.shortcuts import render
from .models import About


def about_view(request):
    """
    Return a response for the About page.

    Args:
        request (HttpRequest): A GET request.

    Returns:
        HttpResponse: Contains the About page.
    """
    about = About.objects.first()
    context = {"about": about}
    return render(request, "about/about.html", context)
