from django.shortcuts import render
from parach_dashboard.forms import StaffSignUpForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def staff_sign_up(request):
    if request.method == 'POST':
        staff_reg_form = StaffSignUpForm(request.POST)
        if staff_reg_form.is_valid():
            staff_reg_form.save()
            return redirect('parach_dashboard:login')
    else:
        staff_reg_form = StaffSignUpForm()
    return render(request, 'parachapp/staff_signup.html', {'staff_reg_form':staff_reg_form})

def login_request(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                if user.is_staff == True:
                    return redirect(reverse('parach_dashboard:dashboard'))
                elif user.is_superuser:
                    return redirect('parach_dashboard:dashboard')
            else:
                messages.error(request, "Invalid Login Credentials!")
                #return HttpResponseRedirect("/")
                return redirect('parachapp:login')
    else:
        login_form = AuthenticationForm()
    return render(request, 'parachapp/login.html', {'login_form':login_form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("parach_dashboard:login")