from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .forms import UserRegisterForm

# Vista de Inicio de Sesión
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me', None)
        if not remember_me:
            self.request.session.set_expiry(0)  # Expira la sesión al cerrar el navegador
        return super(CustomLoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = UserRegisterForm()  
        return context

# Vista de Cierre de Sesión
class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirige al login tras cerrar sesión

# Vista de Registro
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Tu cuenta ha sido creada! Ahora puedes iniciar sesión.')
            return redirect('login')
        else: 
            messages.error(request, f'¡Tu cuenta NO ha sido creada!')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Vista del Perfil de Usuario
@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

# Vista para cambiar contraseña
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

# Vista para restablecer contraseña
class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/forgot-password.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')

# Vista para confirmar restablecimiento de contraseña
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/recover-password.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
