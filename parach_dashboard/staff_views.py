
from parach_dashboard.models import (Course,Enquiry, Student, User, Instructor, Salary)
from parach_dashboard.forms import (InstructorCreateForm, InstructorUpdateForm)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

def add_instructor(request):
    instructor = Instructor.objects.all()
    
    if request.method == 'POST':
        form = InstructorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'instructor has been created successfully')
            return redirect('parach_dashboard:instructor_home')
    else:
        form = InstructorCreateForm()

    context = {
        'form':form,
        'instructor':instructor
    }
    
    return render(request, 'staff_templates/add_instructor.html',context)

def update_instructor(request,slug):
    instructor = Instructor.objects.get(slug=slug)
    if request.method == 'POST':
        form = InstructorUpdateForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, 'instructor has been updated successfully')
            return redirect('parach_dashboard:instructor_home')
    else:
        form = InstructorUpdateForm(instance=instructor)

    context = {
        'form':form,
        
    }
    
    return render(request, 'staff_templates/update_instructor.html',context)

def delete_instructor(request,slug):
    form = Instructor.objects.get(slug=slug)
    if request.method == 'POST':
        form.delete()
        return redirect('parach_dashboard:instructor_home')
    context = {
        'form':form,
        
    }
    return render(request, 'staff_templates/delete_instructor.html',context)