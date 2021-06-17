from django.db import models
from category.models import Category

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product_name

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(slug__in=ids)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
