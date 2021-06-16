from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message
from utilities.functions import send_email


@receiver(post_save, sender=Message, dispatch_uid="api.models.message.post_save")
def send_thank_you_email(sender, instance, created, **kwargs):
    if created:
        recipients = [instance.email]
        context = dict(name=instance.name)

        send_email(
            subject="Thank you for reaching out!",
            recipients=recipients,
            context=context,
        )
