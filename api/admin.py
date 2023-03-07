from django.contrib import admin
from .models import Company
from .models import Employees

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','description')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name','address','position','about')



admin.site.register(Company,CompanyAdmin)
admin.site.register(Employees,EmployeesAdmin)