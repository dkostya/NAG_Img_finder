from django.db import models

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title



class Image(models.Model):

    url = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
