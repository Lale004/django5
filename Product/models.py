from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField(default=0)
    discount_price=models.FloatField(blank=True,null=True,default=0)

    def __str__(self):
        return self.name
# Create your models here.
