from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(primary_key= True, max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True)

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.CharField(max_length=200)

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_on = models.DateField(auto_now=True)
    content = models.TextField()

    class meta:
        ordering = ['-created_on']