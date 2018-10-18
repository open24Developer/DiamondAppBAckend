from django.conf.urls import url
from . import views

app_name='projects'

urlpatterns = [
    url(r'^project/disable/(?P<project_id>[0-9]+)$',views.ProjectApi.as_view()),
    url(r'^project/edit/(?P<project_id>[0-9]+)$',views.ProjectApi.as_view()),
    url(r'^project/detail/(?P<project_id>[0-9]+)$',views.ProjectApi.as_view()),
    url(r'^project/list$',views.ProjectApi.as_view()),
    url(r'^project/create$',views.ProjectApi.as_view()),
    ]
