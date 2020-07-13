from django.shortcuts import redirect, render

# Create your views here.
from .models import Profile
from .forms import SingUp, UserForm , UserProfile
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.contrib.auth.decorators import login_required

def sing_up(request):
    if request.method == 'POST':
        form = SingUp(request.POST , request.FILES)
        if form.is_valid:
            form.save()
            user = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(user=user,password=password)
            login(request,user)
            return redirect('/accounts/profile/edit/')
    else:
        form = SingUp()
    context = {'form':form}
    return render(request,'accounts/singup.html',context)

@login_required
def profile_information(request):
    profile_info = Profile.objects.get(user=request.user)
    context = {'profile':profile_info}
    return render(request,'accounts/profile.html',context)

@login_required
def edit_profile(request):
    profile_info = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form1 = UserForm(request.POST , request.FILES , instance=request.user) 
        form2 = UserProfile(request.POST , request.FILES , instance=profile_info)
        if form1.is_valid and form2.is_valid:
            form1.save()
            myform2 = form2.save(commit=False)
            myform2.user = request.user
            myform2.save()
            return redirect('/accounts/profile')
    else:
        form1 = UserForm(instance=request.user) 
        form2 = UserProfile(instance=profile_info)
    context = {'user':form1 , 'profile':form2 }
    return render(request,'accounts/edit_Profile.html',context)