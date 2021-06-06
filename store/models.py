from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=125)
    description = models.TextField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.product_name

