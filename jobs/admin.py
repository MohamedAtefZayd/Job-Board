from django.contrib import admin

# Register your models here.
from .models import job,apply_job
admin.site.register(job)
admin.site.register(apply_job)