#craete by me

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SingUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2',]
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class UserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user','location')