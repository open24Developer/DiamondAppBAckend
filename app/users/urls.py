from django.conf.urls import url
from . import views

app_name='users'

urlpatterns = [
    url(r'^user/changepassword$',views.ChangePassword.as_view()),
    url(r'^user/login$',views.LoginApi.as_view()),
    url(r'^user/edit/(?P<user_id>[0-9]+)$',views.UserApi.as_view()),
    url(r'^user/disable/(?P<user_id>[0-9]+)$',views.UserApi.as_view()),
    url(r'^user/create$',views.UserApi.as_view()),
    url(r'^user/forgotpassword$',views.ChangePassword.as_view()),

]
