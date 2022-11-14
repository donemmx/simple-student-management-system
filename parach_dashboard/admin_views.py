from parach_dashboard.models import (BranchLocation, Course,Enquiry, Student, User, Instructor, Salary)
from parach_dashboard.forms import (EnquiryCreateForm,EnquiryUpdateForm, StudentCreateForm,  CreateCourseForm, UpdateCourseForm)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
import csv
import datetime
from datetime import date, timedelta

def adminhome(request):
    
    course = Course.objects.all()
    student = Student.objects.all()
    student_count = Student.objects.all().count()
    enquiry_count = Enquiry.objects.all().count()
    #teacher_count = Teacher.objects.all().count()
    

   
    completed_payments = Student.objects.filter(payment_status='Fully Paid').count()
    pending_payments = Student.objects.filter(payment_status='Not Fully Paid').count()
    

    context ={
        'student':student,
        'course':course,
        'student_count':student_count,
        'enquiry_count':enquiry_count,
        #'teacher_count':teacher_count,
        'completed_payments':completed_payments,
        'pending_payments':pending_payments,
       
        
        
    }
    return render(request, 'admin_templates/admin-home.html', context)

def generate_students(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename=students.csv'

    writer = csv.writer(response)
    student = Student.objects.all()
    writer.writerow(['firstname', 'lastname', 'mobile_phone', 'email', 'address', 'Date Downloaded'])
    for students in student:
        writer.writerow([students.firstname, students.lastname, students.mobile_phone, students.email, students.address, date.today()])
    return response

def branch_detail(request,slug):
    locations = BranchLocation.objects.get(slug=slug)
    students = Student.objects.filter(branch=locations)
    context = {
        'locations':locations,
        'students':students,
    }
    return render(request, 'admin_templates/location.html', context)

def enquiry_home(request):
    #students = Enquiry.objects.order_by('-enquiry_date')[:4]
    students = Enquiry.objects.all()
    context = {
        'students':students,
    }
    return render(request, 'admin_templates/enquiry_home.html', context)
    

def create_enquiry(request):
    if request.method == 'POST':
        form = EnquiryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'a new enquiry has been created')
            return redirect('parach_dashboard:enquiry_home')
    else:
        form = EnquiryCreateForm()
    
    return render(request, 'admin_templates/create_equiry.html',{'form':form,})

def update_enquiry(request,slug):
    student = Enquiry.objects.get(slug=slug)
    if request.method == 'POST':
        student_update_form = EnquiryUpdateForm(request.POST, instance=student)
        if student_update_form.is_valid():
            student_update_form.save()
            
            return redirect(reverse('parach_dashboard:enquiry_home'))
    else:
    
        student_update_form = EnquiryUpdateForm(instance=student)
        

    context = {
        
        'student_update_form':student_update_form
        
    }

    return render(request, 'admin_templates/update_enquiry.html',context)

#delete view for enquiry
def delete_enquiry(request,slug):
    student = Enquiry.objects.get(slug=slug)
    student_delete_form = Enquiry.objects.get(slug=slug)
    if request.method == 'POST':
        student_delete_form.delete()
        return redirect('parach_dashboard:enquiry_home')
    context = {
        'student_delete_form':student_delete_form,
        'student':student
    }

    return render(request, 'admin_templates/delete_enquiry.html',context)

def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'A new student has been added succesfully!')
            return redirect('parach_dashboard:student_home')
    else:
        form = StudentCreateForm()
    
    return render(request, 'admin_templates/createstudent.html',{'form':form,})

def student_home(request):
    students = Student.objects.order_by('-amountpaid')[:10]
    context = {
        'students':students,
    }
    return render(request, 'admin_templates/student_home.html', context)

    # teacher views

def instructor_home(request):
    instructors = Instructor.objects.order_by('-date_joined')[:4]
    context = {
        'instructors':instructors,
    }
    return render(request, 'admin_templates/instructor_home.html', context)




def create_course(request):
    course = Course.objects.all()
    
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New course has been created successfully')
            return redirect('.')
    else:
        form = CreateCourseForm()

    context = {
        'form':form,
        'course':course
    }
    
    return render(request, 'admin_templates/add_course.html',context)



def update_course(request,slug):
    course = Course.objects.get(slug=slug)
    if request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course has been updated successfully')
            return redirect('parach_dashboard:create_course')
    else:
        form = UpdateCourseForm(instance=course)

    context = {
        'form':form,
        
    }
    
    return render(request, 'admin_templates/update_course.html',context)

def delete_course(request,slug):
    form = Course.objects.get(slug=slug)
    if request.method == 'POST':
        form.delete()
        return redirect('parach_dashboard:create_course')
    context = {
        'form':form,
        
    }
    return render(request, 'admin_templates/delete_course.html',context)

# location Views
def orogun(request):
    #students = Student.objects.filter(branch__iexact=students.branch.branch_name).order_by('-students')[:10]
   
    students = Student.objects.filter(branch=self.branch.branch_name)
    return render(request, 'admin_templates/orogun.html', {'students':students})

