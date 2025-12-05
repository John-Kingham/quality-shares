from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    """Returns a response with a test message."""
    return HttpResponse("blog app is working")
