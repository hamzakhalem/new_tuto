from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=300, null=True, blank=True)
    ecity = models.CharField(max_length=300, null=True, blank=True)
    esalary = models.FloatField(null=True,)

class Customer(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=300, null=True, blank=True)


     
