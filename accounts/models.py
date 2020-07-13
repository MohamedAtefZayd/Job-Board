from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True , help_text='Example : 2002-12-29' )
    city = models.CharField(max_length=255,blank=True, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    address = models.CharField(max_length=100,blank=True, null=True)
    address_more = models.CharField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True , help_text='Example : +20 the number')
    fax_number = PhoneNumberField(blank=True, null=True , help_text='Example : +20 the number')
    image = models.ImageField(upload_to='profile_im/', blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)