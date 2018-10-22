from django.conf.urls import url
from . import views

app_name='employee'

urlpatterns = [
    # url(r'^employee/disable/(?P<project_id>[0-9]+)$',views.ProjectApi.as_view()),
    url(r'^employee/edit/(?P<employee_id>[0-9]+)$',views.EmployeeApi.as_view()),
    url(r'^employee/detail/(?P<employee_id>[0-9]+)$',views.EmployeeApi.as_view()),
    url(r'^employee/list$',views.EmployeeApi.as_view()),
    url(r'^employee/create$',views.EmployeeApi.as_view()),
    ]
