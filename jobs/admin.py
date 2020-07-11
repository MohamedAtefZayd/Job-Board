from django.contrib import admin

# Register your models here.
from .models import job,City,Country,apply_job
admin.site.register(job)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(apply_job)