from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    deleted_val = models.EmailField(null=True,blank=True)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'user_profile'

