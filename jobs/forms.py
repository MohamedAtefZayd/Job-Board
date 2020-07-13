from django import forms
from .models import apply_job,job

class apply(forms.ModelForm):
    class Meta:
        model = apply_job
        fields = ['name','email','cv','description','website','Experience',]
        
        
class AddJob(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('created_by','location_city','location_country','created_at','slug',)
        