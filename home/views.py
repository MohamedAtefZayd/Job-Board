from django.shortcuts import render

# Create your views here.
from jobs.models import job
from django.core.paginator import Paginator
from .filters import ProductFilter

def home_list(request):
    jobList = job.objects.all()
    filter = ProductFilter(request.GET, queryset=jobList)
    jobList = filter.qs
    paginator = Paginator(jobList, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"jobs": jobList , 'job_l':page_obj , 'filter': filter }
    return render(request,'home/home.html',context)