from django.db import models

# Create your models here.

class Car(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product-image")
    def __str__(self) -> str:
        return self.title
