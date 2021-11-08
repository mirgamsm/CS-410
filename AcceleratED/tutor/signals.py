from django.db.models.signals import post_save
from .models import User, Tutor
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_Tutor(sender, instance, created, **kwargs):
    if created:
        Tutor.objects.create(email=instance)


@receiver(post_save, sender=User)
def create_Tutor(sender, instance, **kwargs):
    instance.tutor.save()
