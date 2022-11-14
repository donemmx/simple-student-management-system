from django.contrib.auth.models import AbstractUser
from django.core.checks import messages
from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import OrderBy
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify 
import random
import string
#from dateHelpers.models import DateHelper

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


class BranchLocation(models.Model):
    branch_name = models.CharField(max_length=200, default='Orogun')
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.branch_name

    def get_absolute_url(self):
        return reverse("branch_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.branch_name)
        return super().save(*args, **kwargs)

class Course(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(null=False)
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("create_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        new_letters = string.ascii_lowercase
        generate_letters = ''.join(random.choices(new_letters + string.digits, k=10))
        
        if not self.slug:
            self.slug = slugify(self.name + generate_letters)
        return super().save(*args, **kwargs)


class Enquiry(models.Model):
    
    full_name = models.CharField(max_length=255)
    mobile_phone = models.BigIntegerField()
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    branch = models.ForeignKey(BranchLocation, null=True, on_delete=models.SET_NULL)
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=7, choices=GENDER, default='Male')
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(null=False)
    
    
   
    #enquiry_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.full_name)

    def get_absolute_url(self):
        return reverse("enquiry_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        new_letters = string.ascii_lowercase
        generate_letters = ''.join(random.choices(new_letters + string.digits, k=10))
        if not self.slug:
            self.slug = slugify(self.full_name + generate_letters)
        return super().save(*args, **kwargs)

class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    mobile_phone = models.BigIntegerField(blank=True, null=True, default='070')
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    #bio = models.TextField(null = True, blank=True, default='write about yourself here (optional)')
    branch = models.ForeignKey(BranchLocation, null=True, on_delete=models.SET_NULL)
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=7, choices=GENDER, default='Male')
    profile_pic = models.ImageField( upload_to = 'Profile_pics', null = True, blank = True)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(null=False)
    #session = models.ForeignKey(StudySession, on_delete=models.CASCADE)
    #amountpaid = models.DecimalField(max_digits=9, decimal_places=2, default='000000.00',null=True, blank=True)
    
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
    amountpaid = models.DecimalField(max_digits=8, decimal_places=2, default='0000000.00',null=True, blank=True)

    
    STATUS = (
        ('Fully Paid', 'Fully Paid'),
        ('Not Fully Paid', 'Not Fully Paid'),
        
    )
    payment_status = models.CharField(max_length=16, choices=STATUS, default="Not Fully Paid")
    completed_course = models.BooleanField(default=False, null=True, blank=True)
    #date_paid = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.firstname)

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        new_letters = string.ascii_lowercase
        generate_letters = ''.join(random.choices(new_letters + string.digits, k=10))
        if not self.slug:
            self.slug = slugify(self.firstname + self.lastname + generate_letters)
        return super().save(*args, **kwargs)

class Instructor(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    mobile_phone = models.BigIntegerField(blank=True, null=True, default='070')
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    GENDER = (
        ('m', 'male'),
        ('f', 'female')
    )
    gender = models.CharField(max_length=5, choices=GENDER, default='male')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    slug = models.SlugField(null=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        new_letters = string.ascii_lowercase
        generate_letters = ''.join(random.choices(new_letters + string.digits, k=10))
        if not self.slug:
            self.slug = slugify(self.firstname + self.lastname + generate_letters)
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.firstname)

class Salary(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.teacher.firstname}, {self.amount}'