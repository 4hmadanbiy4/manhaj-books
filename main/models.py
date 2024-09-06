from django.db import models
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)