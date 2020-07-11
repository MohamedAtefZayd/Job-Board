from django import forms
from .models import apply_job

class apply(forms.ModelForm):
    class Meta:
        model = apply_job
        fields = ['name','email','cv','description','website','Experience',]
        