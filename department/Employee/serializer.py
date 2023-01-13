from rest_framework import serializers
from .models import Department, Employee


class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        feilds = ('dept_id', 'dept_name')


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        feilds = ('emp_id', 'emp_name', 'dept',
                  'dateofjoining', 'photofilename')
