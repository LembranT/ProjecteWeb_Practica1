from django.shortcuts import render


# Create your views here.
def autentication(request):
    return render(request, "autTemplate.html")


def home(request):
    return render(request, "homeTemplate.html")
