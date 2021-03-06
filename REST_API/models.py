from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=220, unique=True)
    descriptions= models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.IntegerField()
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name