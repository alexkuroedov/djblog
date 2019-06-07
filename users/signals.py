from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(signal = post_save, sender = User)
def create_profile(sendet, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(signal = post_save, sender = User)
def save_profile(sendet, instance, **kwargs):
    instance.profile.save()
