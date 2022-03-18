from django.shortcuts import render

# Create your views here.

# Autentication and register
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm


class VRegister(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "autTemplate.html", {"form": form})

    def post(self, request):
        pass


def home(request):
    return render(request, "homeTemplate.html")
