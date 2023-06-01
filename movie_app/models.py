from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.price}"

class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('card', 'karta'),
        ('cash', 'gotówka'),
        ('transfer', 'przelew'),
    )
    method = models.CharField(max_length=8, choices=PAYMENT_CHOICES)
    ticket = models.OneToOneField(Ticket,on_delete=models.CASCADE)
    def __str__(self):
        return self.method