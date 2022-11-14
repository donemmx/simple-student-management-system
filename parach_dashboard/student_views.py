from parach_dashboard.models import Student
from parach_dashboard.forms import StudentUpdateForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages


def student_detail(request,slug):
    #uploadfile = UploadFile.objects.all()
    student = Student.objects.get(slug=slug)

    context = {
        'student':student,
    }
 
    return render(request, 'student_template/student_detail.html', context)


def student_update(request,slug):
    student = Student.objects.get(slug=slug)
    if request.method == 'POST':
        student_update_form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if student_update_form.is_valid():
            student_update_form.save()
            
            #return redirect('customuserapp:student_details', pk=pk)
            return redirect(reverse('parach_dashboard:student_details', kwargs={'slug':slug}))
    else:
    
        student_update_form = StudentUpdateForm(instance=student)
        

    context = {
        
        'student_update_form':student_update_form
        
    }

    return render(request, 'student_template/student_update.html',context)

#delete view for students
def student_delete(request,slug):
    student = Student.objects.get(slug=slug)
    student_delete_form = Student.objects.get(slug=slug)
    if request.method == 'POST':
        student_delete_form.delete()
        return redirect('parach_dashboard:student_home')
    context = {
        'student_delete_form':student_delete_form,
        'student':student
    }

    return render(request, 'student_template/student_delete.html',context)

def incomplete_payments(request):
    
    students = Student.objects.filter(payment_status='Not Fully Paid')
    
    context ={
        'students':students
    }
    return render(request, 'student_template/incomplete_payment.html', context)
def completed_payments(request):
    
    students = Student.objects.filter(payment_status='Fully Paid')
    
    context ={
        'students':students
    }
    return render(request, 'student_template/completed_payments.html', context)

