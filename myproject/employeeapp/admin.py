from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Employee, Customer
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'ename', 'ecity']
admin.site.register(Employee, EmployeeAdmin)
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'cname']
admin.site.register(Customer, CustomerAdmin)
admin.site.unregister(Group)

admin.site.site_header = "عنجل راي مريضة"
