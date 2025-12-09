from django.http import HttpResponse


def portfolio(request):
    return HttpResponse("The portfolio view is working.")
