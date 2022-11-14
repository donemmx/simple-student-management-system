from django.urls import path
from . import views
from parach_dashboard import admin_views, staff_views, student_views
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required
app_name = 'parach_dashboard'
urlpatterns = [

    #admin views
    path('', admin_views.adminhome, name='dashboard' ),

    path('staff_sign_up/', views.staff_sign_up, name='staff_sign_up'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name= 'logout'),

    path('create_enquiry/', admin_views.create_enquiry, name='create_enquiry'),
    path('enquiry_home/', admin_views.enquiry_home, name='enquiry_home'),
    path('update_enquiry/<slug:slug>/', admin_views.update_enquiry, name='update_enquiry'),
    path('delete_enquiry/<slug:slug>/', admin_views.delete_enquiry, name='delete_enquiry'),

    path('branch_detail/<slug:slug>/', admin_views.branch_detail, name='branch_detail'),
   
    path('create_student/', admin_views.create_student, name='create_student'),
    path('student-home/', admin_views.student_home, name='student_home'),
    path('generate_students', admin_views.generate_students, name='generate_students'),
    #others
    path('create_course/', admin_views.create_course, name='create_course'),
    #path('create_detail/<slug:slug>/', admin_views.create_detail, name='create_detail'),
    path('update_course/<slug:slug>/', admin_views.update_course, name='update_course'),
    path('delete_course/<slug:slug>/', admin_views.delete_course, name='delete_course'),

     #student views
    path('student_detail/<slug:slug>/', student_views.student_detail, name='student_details'),
    path('update-student/<slug:slug>/', student_views.student_update, name='student_updates'),
    path('student_delete/<slug:slug>/', student_views.student_delete, name='student_delete'),
    path('incomplete_payments/', student_views.incomplete_payments, name='incomplete_payments'),
    path('completed_payments/', student_views.completed_payments, name='completed_payments'),

    #instructor views
    path('instructor_home/', admin_views.instructor_home, name='instructor_home'),
    path('add_instructor/', staff_views.add_instructor, name='add_instructor'),
    path('update_instructor/<slug:slug>/', staff_views.update_instructor, name='update_instructor'),
    path('delete_instructor/<slug:slug>/', staff_views.delete_instructor, name='delete_instructor'),
     # locations
    path('orogun/', admin_views.orogun, name='orogun'),
    
]