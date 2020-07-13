from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.urls import reverse
from .models import job
from django.core.paginator import Paginator
from .forms import apply , AddJob
from datetime import datetime
from django.contrib.auth.decorators import login_required

def job_list(request):
    jobList = job.objects.all()
    paginator = Paginator(jobList, 7) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"jobs": jobList , 'job_l':page_obj}
    return render(request,'jobs/job_list.html',context)

def job_detail(request , id , slug):
    jobDetail = get_object_or_404(job , id=id , slug=slug)
    context = {'job':jobDetail}
    return render(request,'jobs/job_detail.html',context)

@login_required
def applyForm(request , id , slug):
    jobDetail = get_object_or_404(job , id=id , slug=slug)
    if request.method == 'POST':
        form = apply(request.POST , request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.apply_to = jobDetail
            myform.apply_by = request.user
            myform.create_at = datetime.now()
            myform.save()
    else:
            form = apply()
    context = {'job':jobDetail , 'form':form}
    return render(request,'jobs/apply_form.html',context)


def addJob(request):
    if request.method == 'POST':
        form = AddJob(request.POST , request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.created_by = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))    
    else:
        form = AddJob()
    context = {'form':form}
    return render(request,'jobs/postJob.html',context)
