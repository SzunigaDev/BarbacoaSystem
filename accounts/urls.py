from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register, profile, CustomPasswordChangeView, CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('reset-password/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset-password-done/', CustomPasswordResetView.as_view(template_name='accounts/reset_password_done.html'), name='password_reset_done'),
    path('reset-password-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password-complete/', CustomPasswordResetConfirmView.as_view(template_name='accounts/reset_password_complete.html'), name='password_reset_complete'),
]
