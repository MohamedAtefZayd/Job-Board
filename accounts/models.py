from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class SingUp(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birthday = models.DateField()
    