from django.contrib import admin
from parach_dashboard.models import (
    User,Student,
                    BranchLocation,
                    #Attend,
                    Instructor,
                    Course,
                    Student,
                    Enquiry,
                    # StudentAdvancedProfile,
                    Salary
)
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)
    prepopulated_fields = {"slug": ("name",)}
class BranchLocationAdmin(admin.ModelAdmin):
    list_display = ("branch_name",)
    prepopulated_fields = {"slug": ("branch_name",)}

class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname",)
    prepopulated_fields = {"slug": ("firstname",)}
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "course","mobile_phone","address", "branch", "gender")
    prepopulated_fields = {"slug": ("full_name",)}

class InstructorAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname",)
    prepopulated_fields = {"slug": ("firstname",)}
class SalaryAdmin(admin.ModelAdmin):
    list_display = ("instructor", )
    
    
admin.site.register(User)
admin.site.register(Course, CourseAdmin)
admin.site.register(BranchLocation, BranchLocationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Salary, SalaryAdmin)
