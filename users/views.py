from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .form import RegisterForm
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get("username") 
            messages.success(request,f"welcome {username} your account is created")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,'user/register.html',context={"form":form})

@login_required
def profile(request):
    return render(request,'user/profile.html') 
