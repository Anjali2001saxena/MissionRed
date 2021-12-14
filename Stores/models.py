from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    contact = models.CharField(max_length=50)
    location = models.TextField()
    pin_code = models.CharField(max_length=50)
    delivery = models.BooleanField()
    password = models.CharField(max_length=50, null=True)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.CharField(max_length=200)
    address = models.TextField()
    customer = models.CharField(max_length=200)
    timing = models.DateTimeField(auto_now_add=True)
    items = models.TextField()
    status = models.CharField(max_length=200, default = 'Pending')
