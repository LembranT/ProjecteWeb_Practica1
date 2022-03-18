from django.db import models


# Create your models here.
class Reader(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=40)
    mail = models.EmailField()
    password = models.CharField(max_length=150)


class Books(models.Model):
    #idBook = models.IntegerField()     #Es necessita cridar a la api de google.
    name = models.CharField(max_length=20)
    review = models.CharField(max_length=1000)
