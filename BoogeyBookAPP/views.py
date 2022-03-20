from django.http import HttpResponse
from django.shortcuts import render, redirect
from BoogeyBookAPP.models import Book

# Create your views here.

# Autentication and register
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class VRegister(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "autTemplate.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if (form.is_valid):
            user = form.save()  #on es guarda?
            login(request, user)   
            return render(request, "homeTemplate.html")
        else:
            pass

    def login(request):
        return render(request, "loginTemplate.html")


def home(request):
    return render(request, "homeTemplate.html")


def search(request):
    if request.GET["data"]:
        # message="Book searched: %r" %request.GET["data"]
        book = request.GET["data"]

        books = Book.objects.filter(name__icontains=book)

        return render(request, "results.html", {"books": books, "query": book})

    else:
        message = "You just entered nothing."

    return HttpResponse(message)
