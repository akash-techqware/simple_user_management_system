from django import forms
from django.forms import ModelForm
from .models import Employee



class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_name', 'emp_email', 'emp_contact', 'emp_role', 'emp_salary', 'image')
        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Name'}),
            'emp_email': forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Email'}),
            'emp_contact': forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Contact No.'}),
            'emp_role': forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Role'}),
            'emp_salary': forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'Salary'}),
            'image': forms.FileInput(attrs={'class': 'button is-info mt-3',}),
        }
        

