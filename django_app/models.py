from django.db import models

# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=128)
#     author = models.CharField(max_length=200)
#     description = models. CharField(max_length=512, null=True)
#
#
#     page_count = models.IntegerField()
#     price = models.DecimalField( max_digits=6, decimal_places=2)

class Game(models.Model):
    title = models.CharField(max_length=128)
    publisher = models.CharField(max_length=200)
    description = models.CharField(max_length=512, null=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)



