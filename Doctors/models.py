from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    contact = models.CharField(max_length=50)
    specialization = models.CharField(max_length=200)
    registeration_number = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)

class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    slot = models.DateTimeField()
    doctor = models.CharField(max_length=200)
    patient = models.CharField(max_length=200, default=None, blank=True, null=True)
    patient_contact = models.CharField(max_length=200, default=None, blank=True, null=True)
    status = models.CharField(max_length=200, default='Available')
