from django.db.models.signals import post_save
from django.contrib.auth.models import User # this will be the Sender
from django.dispatch import receiver
from .models import Profile


# Everytime a User is created or registered, this is called.
# This creates a Profile object for each User who registered.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Now save the Profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

