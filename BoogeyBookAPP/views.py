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
        user = form.save()
        login(request, user)
        return redirect('Home')


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
