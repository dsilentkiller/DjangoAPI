from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from  rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from  EmployeeApp.models import Departments, Employees
from  EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer 
from EmployeApp.serializers  import DepartmentSerializer,EmployeeSerializer 
from django.core.serializers import default_storage 

@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.methiod == 'POST':
        departments_data = JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=departments_data)
        if DepartmentSerializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failded to add",safe=False)

    elif request.method == "PUT":
        departments_data = JSONParser().parse(request)
        department = Departments.object.get(DepartmentId = departments_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JSONParser("Updated Successfully", safe = False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method =='DELETE':
        department = Departments.objects.get(DepartmentId= id)
        department.delete()
        return JsonResponse("Deleted Successfully!!", safe = False)




@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        Employees_serializer = EmployeeSerializer(Employees, many = True)
        return JsonResponse(Employees_serializer.data, safe=False)
    elif request.methiod == 'POST':
        Employees_data = JSONParser().parse(request)
        Employees_serializer=EmployeeSerializer(data=Employees_data)
        if EmployeeSerializer.is_valid():
            Employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failded to add",safe=False)

    elif request.method == "PUT":
       employees_data = JSONParser().parse(request)
       employee = Employees.object.get(EmployeeId = employees_data['EmployeeId'])
       employees_serializer = EmployeeSerializer(employee, data=employees_data)
       if employees_serializer.is_valid():
        employees_serializer.save()
        return JSONParser("Updated Successfully", safe = False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method =='DELETE':
        employee =Employees.objects.get(EmployeeId= id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name, safe=False)