from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-sm', 
        'placeholder': 'Introduce tu correo electrónico',
        'title': 'Correo'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm', 
                'placeholder': 'Introduce tu nombre de usuario',
                'title': 'Usuario'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control form-control-sm', 
                'placeholder': 'Introduce tu contraseña',
                'title': 'Contraseña'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email
