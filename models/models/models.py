from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mailing_address = models.TextField()

class Order(models.Model):
    order_number = models.IntegerField()
    date = models.DateField()
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
