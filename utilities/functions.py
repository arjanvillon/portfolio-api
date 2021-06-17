import time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def generate_timestamp():
    timestamp = round(time.time())
    return str(timestamp)


def send_email(
    subject,
    recipients,
    sender=settings.EMAIL_HOST_USER,
    bcc=settings.EMAIL_HOST_BCC,
    context=None,
):
    html_template = render_to_string("email.html", context)

    email = EmailMultiAlternatives(
        subject=subject, body=html_template, from_email=sender, to=recipients, bcc=[bcc]
    )

    email.attach_alternative(html_template, "text/html")
    email.send()

    return None
