from django.core.mail import send_mail
from django.conf import settings

def send_email_notification(subject, message, recipient_list):
    """
    Send an email notification using the configured email backend.
    
    :param subject: Subject of the email
    :param message: Body of the email
    :param recipient_list: List of recipient email addresses
    """
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,  # Raises an error if email fails to send
    )
