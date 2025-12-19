from django.http import HttpResponse


def test_view(request):
    return HttpResponse("The About page is working.")
