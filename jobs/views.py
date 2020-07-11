from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import job
from django.core.paginator import Paginator
from .forms import apply
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

