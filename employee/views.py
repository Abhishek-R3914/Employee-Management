from django.shortcuts import render, redirect
from .models import Employee
from . forms import EmployeeForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    
    form = EmployeeForm()
    context = {
        'form': form,
    }    
    return render(request,'add_employee.html', context)

def employee_list(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee,
    }
    return render(request, 'employees.html', context)


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        
    form = EmployeeForm(instance = employee)
    context = {
        'form' : form,
    }
    return render(request, 'edit_employee.html', context)

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')

def active_employees(request):
    employee = Employee.objects.filter(status = 'Active')
    context = {
        'employee' : employee,
    }
    return render(request,'active_employee.html',context)

def employee_detail(request,id):
    employee = Employee.objects.get(id=id)
    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)