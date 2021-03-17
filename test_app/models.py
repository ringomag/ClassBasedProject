from django.db import models
from django import forms

# Create your models here.
class Lik(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + " " + self.lastname
