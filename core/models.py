from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  birth_date = models.DateField(null=True, blank=True, help_text="Share for free stuff")
  ghin = models.CharField(max_length=12, blank=True, help_text="GHIN or OTHER")
  phone = models.CharField(max_length=12, blank=True, help_text="Contact Phone")
  
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
    instance.profile.save()

  
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#   try:
#     instance.profile.save()
#   except ObjectDoesNotExist:
#     return nill

  
  