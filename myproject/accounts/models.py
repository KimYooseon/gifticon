from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prev_saleCheck = models.TextField(max_length=50,blank=True)
    prev_brandCheck = models.TextField(max_length=50,blank=True)
    prev_detail_id = models.IntegerField(null=True ,blank=True)

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, prev_brandCheck='all',prev_saleCheck='all')
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''
    