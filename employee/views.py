from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employee/list.html', context)

def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            emp_name = form.cleaned_data['emp_name']
            if Employee.objects.filter(emp_name=emp_name).exists():
                form.add_error('emp_name', 'This email address is already in use.')
            else:
                form.save()
                return redirect('employees-list')
    context = {
        'form': form,
    }
    return render(request, 'employee/create.html', context)

def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')
    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee/edit.html', context)

def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')
    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)


# def index(request):
#     return render(request, 'index.html')