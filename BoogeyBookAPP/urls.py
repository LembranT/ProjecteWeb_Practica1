from django.urls import path
from views import VRegister
from BoogeyBookAPP import views

urlpatterns = [
    path('', VRegister.as_view(), name="Autentication"),
    path('homeTemplate', views.home),
    path('search/', views.search),
]