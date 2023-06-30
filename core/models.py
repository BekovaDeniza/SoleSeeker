from django.db import models
from jsonfield import JSONField
from parsers.models import Site


class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    properties = JSONField(blank=True, null=True)
    image = models.ImageField(upload_to='sneakers/')
    url = models.URLField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    article = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
