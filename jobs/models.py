from django.db import models
# Create your models here.
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.contrib.auth.models import User
import random
JOB_TYPE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
)

GENDER = (
    ("Male","Male"),
    ("Female","Female"),
    ("Any","Any"),
)

def images_upload(instance , filename):
    point = filename.find(".")
    end_image = filename[int(point):]
    list_id = []
    n = str(random.random())
    for num in list_id:
    	if n != num:
    		list_id.append(n)
    	else:
    		n = str(random.random())
    return "job/%s.%s"%(str(n[2:]) , end_image)
   
class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
        
class job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50 , choices=JOB_TYPE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    country = models.ForeignKey('Country',on_delete=models.CASCADE)
    city = models.ForeignKey('City',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    low_salary = models.PositiveIntegerField(default=0)
    heigh_salary = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=images_upload)
    vacancy = models.PositiveIntegerField(default=0)
    Experience = models.PositiveIntegerField(default=0)
    Gender = models.CharField(max_length=50 , choices=GENDER)
    Deadline = models.DateField()
    description = models.TextField(max_length=2000)
    slug = models.SlugField(blank=True , null=True)
    
    def save(self , *args, **kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args , **kwargs)
        
    def __str__(self):
        return self.title
    

class apply_job(models.Model):
    apply_by = models.ForeignKey(User,on_delete=models.CASCADE)
    apply_to = models.ForeignKey(job , related_name='apply_job' , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    description = models.TextField(max_length=1000)
    create_at = models.DateTimeField()
    Experience = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name