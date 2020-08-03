from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    profile_pic = models.ImageField(default='default.jpg', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = (
        ('indoor', 'indoor'),
        ('outdoor', 'outdoor')
    )
    name = models.CharField(max_length=40, null=True)
    price = models.FloatField(null=True)
    category =models.CharField(max_length=40, null=True, choices=category)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    status = (
        ('Pending','Pending'),
        ('Deliverd', 'Deliverd'),
        ('Out for delivary', 'out for delivary')

    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    status = models.CharField(max_length=200, null=True, choices=status)
    note = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.customer.name
