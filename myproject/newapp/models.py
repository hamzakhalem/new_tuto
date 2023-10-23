from django.db import models

# Create your models here.
class Registration(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.fname
    