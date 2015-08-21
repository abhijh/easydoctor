from django.db import models

class doctor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    displayName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    emailId = models.EmailField(max_length=30)