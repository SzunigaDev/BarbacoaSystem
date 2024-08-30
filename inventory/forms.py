from django import forms
from .models import Product, Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_name', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter supplier name'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter contact name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter email address'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'reorder_level', 'supplier']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter product description', 'rows': 4}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter quantity'}),
            'reorder_level': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter reorder level'}),
            'supplier': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }
