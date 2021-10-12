from django.db import models
from django.db.models.expressions import CombinedExpression
from datetime import datetime

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

class ClinicalData(models.Model):
    componentnames = [('hw','Height/Weight'),('bp','Blood Pressure'),('hr','Heart Rate')]
    componentname = models.CharField(choices=componentnames,max_length=10)
    componentvalue = models.CharField(max_length=10)
    measureddate = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    