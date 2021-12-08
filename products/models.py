from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'categories'


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField() 
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, related_name='products', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})
    