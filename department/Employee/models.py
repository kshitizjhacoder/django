from django.db import models

# Create your models here.


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=200, default=None)


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=200, default=None)
    dept = models.CharField(max_length=200, default=None)
    dateofjoing = models.DateField()
    photofilename = models.CharField(max_length=50)
