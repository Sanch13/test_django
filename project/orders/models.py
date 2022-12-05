from django.contrib.auth.models import User
from django.db import models
from products.models import Products


class SalesOrders(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Products)
