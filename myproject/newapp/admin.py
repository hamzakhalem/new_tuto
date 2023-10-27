from django.contrib import admin
from .models import Registration, Employee
# Register your models here.
class RegistartionAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'city', "email"]
admin.site.register(Registration, RegistartionAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'ename', 'ecity', "esalary"]
admin.site.register(Employee, EmployeeAdmin)