from django.contrib import admin

# Register your models here.
# the module name is app_name.models
from dept_emp.models import Department, Employee

# this class define which department columns will be shown in the department admin web site.
class DepartmentAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'dept_name', 'dept_desc']
    # define search columns list, then a search box will be added at the top of Department list page.
    search_fields = ['dept_name', 'dept_desc']
    # define filter columns list, then a filter widget will be shown at right side of Department list page.
    list_filter = ['dept_name']


# this class define employee columns that will be shown in the employee admin web site. Note the foreign key value will be displayed automatically.
# the foreign key is user and dept which reference other model, so the user or department model's __str__(self) method will be called and the return value will be displayed.
class EmployeeAdmin(admin.ModelAdmin):
    # a list of displayed columns name, the user and dept foreign key will display related model's __str__(self) method returned string value.
    list_display = ['id', 'user', 'dept', 'emp_mobile','emp_salary','emp_onboard_date']

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

