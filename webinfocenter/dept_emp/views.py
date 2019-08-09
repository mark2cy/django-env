from django.shortcuts import render

# Create your views here.
from dept_emp.models import Department, Employee
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def home_page(request):
    return render(request, 'dept_emp/home_page.html')
def user_login(request):
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()
    error_message_login_user_name = ''
    error_message_login_password = ''
    if len(username) == 0:
        error_message_login_user_name = 'User name can not be empty.'
    if len(password) == 0:
        error_message_login_password = 'Password can not be empty.'
    if len(username) == 0 or len(password) == 0:
        return render(request, 'dept_emp/home_page.html', {'error_message_login_user_name': error_message_login_user_name, 'error_message_login_password':error_message_login_password})
    else:
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            # login user account.
            auth.login(request, user)
            if user.is_superuser:
                return user_list(request)
            else:
                user.password = password
                return render(request, 'dept_emp/home_page.html',
                              {'error_message_login_user_name': 'This user is not superuser, access is denied.', 'user':user})
        else:
            user = User()
            user.username = username
            user.password = password
            error_json = {'error_message': 'User name or password is not correct.', 'user':user}
            return render(request, 'dept_emp/home_page.html', error_json)
        '''
        # get user by username
        user_list = User.objects.filter(username=username)
        if len(user_list) == 0:
            return render(request, 'dept_emp/home_page.html',{'error_message_login_user_name': 'User name do not exist.'})
        else:
            for user in user_list:
                if user.password == password:
                    if user.is_superuser:
                        return user_list(request)
                    else:
                        return render(request, 'dept_emp/home_page.html',
                                      {'error_message_login_user_name': 'This user is not superuser, access is denied.'})
                else:
                    return render(request, 'dept_emp/home_page.html',
                                  {'error_message_login_password': 'Password is not correct.'})
        '''
def user_logout(request):
    auth.logout(request)
    return render(request, 'dept_emp/home_page.html')
@login_required()
def user_list(request):
    # list all users.
    user_list = User.objects.all()
    return render(request, 'dept_emp/user_list.html',
                      {'user_list': user_list})
@login_required()
def user_pre_add(request):
    return render(request, 'dept_emp/user_pre_add.html')
@login_required()
def user_add(request):
    name = request.POST.get('name','').strip()
    password = request.POST.get('password', '').strip()
    email = request.POST.get('email', '').strip()
    user = User()
    user.username = name
    user.password = password
    user.email = email
    error_message_username = ''
    error_message_password = ''
    error_message_email = ''
    if len(name) == 0:
        error_message_username += 'User name can not be empty.'
    if len(password) == 0:
        error_message_password += 'Password can not be empty.'
    if len(email) == 0:
        error_message_email += 'Email can not be empty.'
    if len(error_message_username) > 0 or len(error_message_password) > 0 or len(error_message_email) > 0:
        return render(request, 'dept_emp/user_pre_add.html',
                      {'error_message_username': error_message_username, 'error_message_password':error_message_password, 'error_message_email':error_message_email, 'user': user})
    else:
        user_exist_list = User.objects.filter(username=name)
        print(len(user_exist_list))
        # the user name exist.
        if len(user_exist_list) > 0:
            return render(request, 'dept_emp/user_pre_add.html', {'error_message':'User name exist, please choose another one.', 'user':user})
        else:
            user.is_staff = True
            user.is_active = True
            user.save()
            return user_list(request)
@login_required()
def user_delete(request):
    del_id_list = get_checked_checkbox_value(request, 'user_')
    for user_id in del_id_list:
        user = User.objects.get(id=user_id)
        user.delete()
    return user_list(request)
def get_checked_checkbox_value(request, check_value_prefix):
    checked_id_list = list()
    for item in request.POST.items():
        print(item)
        if len(item) == 2:
            try:
                index = item[0].index(check_value_prefix)
                if index >= 0:
                    checked_id_list.append(item[0][index + len(check_value_prefix)])
            except ValueError as ex:
                print(ex)
    return checked_id_list
@login_required()
def dept_list(request):
    # list all department.
    dept_list = Department.objects.all()
    return render(request, 'dept_emp/dept_list.html',
                      {'dept_list': dept_list})
@login_required()
def dept_pre_add(request):
    return render(request, 'dept_emp/dept_pre_add.html')
@login_required()
def dept_add(request):
    dept_name = request.POST.get('dept_name','').strip()
    dept_desc = request.POST.get('dept_desc', '').strip()
    dept = Department()
    dept.dept_name = dept_name
    dept.dept_desc = dept_desc
    error_message_dept_name = ''
    if len(dept_name) == 0:
        error_message_dept_name += 'Department name can not be empty.'
    if len(error_message_dept_name) > 0:
        return render(request, 'dept_emp/dept_pre_add.html',
                      {'error_message_dept_name': error_message_dept_name, 'dept': dept})
    else:
        dept_exist_list = Department.objects.filter(dept_name=dept_name)
        print(len(dept_exist_list))
        # the department name exist.
        if len(dept_exist_list) > 0:
            return render(request, 'dept_emp/dept_pre_add.html', {'error_message':'The department name exist, please choose another one.', 'dept':dept})
        else:
            dept.save()
            return dept_list(request)
@login_required()
def dept_delete(request):
    del_id_list = get_checked_checkbox_value(request, 'dept_')
    for dept_id in del_id_list:
        dept = Department.objects.get(id=dept_id)
        dept.delete()
    return dept_list(request)
@login_required()
def emp_list(request, dept_id=-1):
    # list all employee.
    if dept_id == -1:
        emp_list = Employee.objects.all()
        print(emp_list)
        return render(request, 'dept_emp/emp_list.html',
                      {'emp_list': emp_list})
    # list special department employee.
    else:
        # return the employee list of this department.
        emp_list = Employee.objects.filter(dept_id==dept_id)
        return render(request, 'dept_emp/emp_list.html',
                      {'emp_list': emp_list})
@login_required()
def emp_pre_add(request):
    user_list = User.objects.all()
    dept_list = Department.objects.all()
    return render(request, 'dept_emp/emp_pre_add.html', {'user_list':user_list, 'dept_list':dept_list})
@login_required()
def emp_add(request):
    emp_user_id = request.POST.get('emp_user_id','').strip()
    emp_dept_id = request.POST.get('emp_dept_id','').strip()
    emp_mobile = request.POST.get('emp_mobile', '').strip()
    emp_salary = request.POST.get('emp_salary','').strip()
    emp_user = User.objects.get(id=emp_user_id)
    emp_dept = Department.objects.get(id=emp_dept_id)
    emp = Employee()
    emp.user = emp_user
    emp.dept = emp_dept
    emp.emp_mobile = emp_mobile
    emp.emp_salary = emp_salary
    error_message_emp_mobile = ''
    emp_exist_list = Employee.objects.filter(emp_mobile=emp_mobile)
    print(len(emp_exist_list))
    # the department name exist.
    if len(emp_exist_list) > 0:
        user_list = User.objects.all()
        dept_list = Department.objects.all()
        return render(request, 'dept_emp/emp_pre_add.html', {'error_message_emp_mobile':'The mobile number has been used, please use another one.', 'emp':emp, 'user_list':user_list, 'dept_list':dept_list})
    else:
        emp.save()
        return emp_list(request)
@login_required()
def emp_delete(request):
    del_id_list = get_checked_checkbox_value(request, 'emp_')
    for emp_id in del_id_list:
        emp = Employee.objects.get(id=emp_id)
        emp.delete()
    return emp_list(request)

