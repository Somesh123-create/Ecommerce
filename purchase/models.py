from django.contrib.auth.models import User
from django.db import models
from store.models import Product
# Create your models here.


class Ordered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.user)
