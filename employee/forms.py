from django import forms
from django.forms import ModelForm, ClearableFileInput
from .models import Employee
from django.utils.html import format_html
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
            'image': forms.ClearableFileInput(attrs={'class': 'button is-info mt-3'}),
        }

