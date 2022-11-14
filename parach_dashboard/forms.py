from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import transaction
from django.db.models import fields


from parach_dashboard.models import (Enquiry, Student, User, 
                                Course, 
                                BranchLocation, Instructor, Salary
                                )
from django.core.exceptions import ValidationError
import datetime
from datetime import date


#student account update
class EnquiryCreateForm(forms.ModelForm):
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'create a username'}))
    
    class Meta:
        model = Enquiry
        exclude = ['slug']

class EnquiryUpdateForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        exclude = ['slug']
class StudentCreateForm(forms.ModelForm):
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'create a username'}))
    
    class Meta:
        model = Student
        exclude = ['slug']


class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['slug']

class InstructorCreateForm(forms.ModelForm):
    class Meta:
        model = Instructor
        exclude = ['slug']


class InstructorUpdateForm(forms.ModelForm):

    class Meta:
        model = Instructor
        exclude = ['slug']


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'price',
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name_match = Course.objects.filter(name=name).exists()  
        if self.instance and not name_match:
            return name
        else:
            raise forms.ValidationError(f'the course "{name}" already exists in database. Please check and update if necessary.')
        
class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'price',
            
        ]


# sign up forms
class StaffSignUpForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'create a username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))
    
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        #if commit:
          #  user.save()
        #teacher = Teacher.objects.create(user=user,course=Course.objects.get(id=1), profile_pic='Profile_pics/3.jpg')
        return user
