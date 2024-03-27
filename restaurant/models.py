from django.db import models

# Create your models here.

class Menu(models.Model):
    Title = models.CharField(max_length =255)
    Price = models.DecimalField() 
    Inventory = models.IntegerField()

class Booking(models.Model):
    Name = models.CharField(max_length =255)
    No_of_guests = models.IntegerField() 
    BookingDate = models.DateTimeField()
    