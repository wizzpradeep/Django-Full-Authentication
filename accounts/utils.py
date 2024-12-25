from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_email_to_(request, email, token):
    subject = "Verify Your Account"
    current_site = get_current_site(request)
    verification_url = f"http://{current_site}/email_verify/{token}"

    body = f"""
    Hello,

    Please verify your email address by clicking the link below:

    {verification_url}

    If you did not request this email, please ignore it.

    Thank you,
    The Team
    """
    sender = settings.EMAIL_HOST_USER
    receiver = [email]

    try:
        send_mail(subject, body, sender, receiver, fail_silently=False)
        logger.info(f"Verification email sent to {email}")
    except Exception as e:
        logger.error(f"Error sending email to {email}: {e}")
        raise 
