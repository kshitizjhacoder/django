from .serializer import Employeeserializer, Departmentserializer
from .models import Employee, Department
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = Departmentserializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        department_serializer = Departmentserializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Sucessfully !!", safe=False)
        return JsonResponse("Failed to store into database", safe=False)
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Department.objects.get(dept_id=department_data['dept_id'])
        department_serializer = Departmentserializer(
            department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updates Sucessfully !!", safe=False)
        return JsonResponse("Failed to update into database", safe=False)
    elif request.method == 'DELETE':
        department = Department.objects.get(dept_id=id)
        department.delete()
        return JsonResponse('Deleted sucessfully!!', safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = Employeeserializer(employeees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employee_serializer = Employeeserializer(data=department_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
        return JsonResponse("Added Sucessfully !!", safe=False)
        return JsonResponse("Failed to store into database", safe=False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(emp_id=employee_data['emp_id'])
        employee_serializer = Employeeserializer(
            employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updates Sucessfully !!", safe=False)
        return JsonResponse("Failed to update into database", safe=False)
    elif request.method == 'DELETE':
        employee = Employee.objects.get(emp_id=id)
        Employee.delete()
        return JsonResponse('Deleted sucessfully!!', safe=False)


def SaveFile(request):
    files = request.FILES["myFile"]
    file_name = default_storage.save(files.name, files)
    return JsonResponse(file_name, safe=True)
