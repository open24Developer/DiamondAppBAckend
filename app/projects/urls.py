from django.conf.urls import url
from . import views

app_name='projects'

urlpatterns = [
    url(r'^project/disable/(?P<project_id>[0-9]+)$',views.ProjectDisable.as_view()),
    url(r'^project/edit/(?P<project_id>[0-9]+)$',views.ProjectEdit.as_view()),
    url(r'^project/detail/(?P<project_id>[0-9]+)$',views.ProjectDeatil.as_view()),
    url(r'^project/list$',views.ProjectList.as_view()),
    url(r'^project/create$',views.ProjectApi.as_view()),
    ]
