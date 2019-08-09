from django.conf.urls import url
from django.urls import path
# import views from local directory.
from . import views
urlpatterns = [
    # do not use empty string in the url request path, it will intercept all request url with all request path value.
    # url(r'', views.home_page, name='home_page'),
    # if you want to intercept the django app root path request just use url path r'^$' to map it.
    # Then following url mapping will handle request http://127.0.0.1:8000/ with view function home_page.
    url(r'^$', views.home_page, name='home_page'),
    # request http://127.0.0.1:8000/dept_emp/user_list will invoke the user_list function defined in views.py.
    url(r'^user_list/', views.user_list, name='user_list'),
    # request http://127.0.0.1:8000/dept_emp/user_pre_add will invoke the user_pre_add function defined in views.py.
    url(r'^user_pre_add/', views.user_pre_add, name='user_pre_add'),
    # request http://127.0.0.1:8000/dept_emp/user_add will invoke the user_add function defined in views.py.
    url(r'^user_add/', views.user_add, name='user_add'),
    # request http://127.0.0.1:8000/dept_emp/user_delete/ will invoke the user_delete function defined in views.py.
    url(r'^user_delete/', views.user_delete, name='user_delete'),
    # request http://127.0.0.1:8000/dept_emp/user_login will invoke the user_login function defined in views.py.
    url(r'^user_login/', views.user_login, name='user_login'),
    # request http://127.0.0.1:8000/dept_emp/user_logout will invoke the user_logout function defined in views.py.
    url(r'^user_logout/', views.user_logout, name='user_logout'),
    # request http://127.0.0.1:8000/dept_emp/dept_list will invoke the dept_list function defined in views.py.
    url(r'^dept_list/', views.dept_list, name='dept_list'),
    # request http://127.0.0.1:8000/dept_emp/dept_pre_add will invoke the dept_pre_add function defined in views.py.
    url(r'^dept_pre_add/', views.dept_pre_add, name='dept_pre_add'),
    # request http://127.0.0.1:8000/dept_emp/dept_add will invoke the dept_add function defined in views.py.
    url(r'^dept_add/', views.dept_add, name='dept_add'),
    # request http://127.0.0.1:8000/dept_emp/dept_delete/ will invoke the dept_delete function defined in views.py.
    url(r'^dept_delete/', views.dept_delete, name='dept_delete'),
    # request http://127.0.0.1:8000/dept_emp/emp_list will invoke the emp_list function defined in views.py.
    url(r'^emp_list/$', views.emp_list, name='emp_list'),
    # request http://127.0.0.1:8000/dept_emp/emp_pre_add will invoke the emp_pre_add function defined in views.py.
    url(r'^emp_pre_add/', views.emp_pre_add, name='emp_pre_add'),
    # request http://127.0.0.1:8000/dept_emp/emp_add will invoke the emp_add function defined in views.py.
    url(r'^emp_add/', views.emp_add, name='emp_add'),
    # request http://127.0.0.1:8000/dept_emp/emp_delete will invoke the emp_delete function defined in views.py.
    url(r'^emp_delete/', views.emp_delete, name='emp_delete'),
]
