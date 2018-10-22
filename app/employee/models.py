from django.db import models
from datetime import datetime


class Employee(models.Model):

    employee_id =  models.CharField(max_length=255,null=True,blank=True)
    first_name =  models.CharField(max_length=255,null=True,blank=True)
    middle_name =  models.CharField(max_length=255,null=True,blank=True)
    last_name =  models.CharField(max_length=255,null=True,blank=True)
    prior_last_name =  models.CharField(max_length=255,null=True,blank=True)
    suffix =  models.CharField(max_length=255,null=True,blank=True)
    address_1 =  models.CharField(max_length=255,null=True,blank=True)
    address_2 =  models.CharField(max_length=255,null=True,blank=True)
    city =  models.CharField(max_length=255,null=True,blank=True)
    state =  models.CharField(max_length=255,null=True,blank=True)
    zip_code =  models.CharField(max_length=255,null=True,blank=True)
    country =  models.CharField(max_length=255,null=True,blank=True)
    disability =  models.CharField(max_length=255,null=True,blank=True)
    ethnicity =  models.CharField(max_length=255,null=True,blank=True)
    gender =  models.CharField(max_length=255,null=True,blank=True)
    smoker =  models.CharField(max_length=255,null=True,blank=True)
    veteran =  models.CharField(max_length=255,null=True,blank=True)
    birth_date =  models.CharField(max_length=255,null=True,blank=True)
    employee_status_effective_date =  models.CharField(max_length=255,null=True,blank=True)
    employee_status =  models.CharField(max_length=255,null=True,blank=True)
    hire_date =  models.CharField(max_length=255,null=True,blank=True)
    rehire_date =  models.CharField(max_length=255,null=True,blank=True)
    termination_date =  models.CharField(max_length=255,null=True,blank=True)
    user_account_deactivation_date =  models.CharField(max_length=255,null=True,blank=True)
    annual_salary =  models.FloatField(null=True,blank=True)
    cost_code =  models.IntegerField(null=True,blank=True)
    department =  models.CharField(max_length=255,null=True,blank=True)
    division =  models.CharField(max_length=255,null=True,blank=True)
    eeo_class =  models.FloatField(null=True,blank=True)
    employment_type =  models.CharField(max_length=255,null=True,blank=True)
    is_supervisor_reviewer =  models.CharField(max_length=255,null=True,blank=True)
    job_title =  models.CharField(max_length=255,null=True,blank=True)
    position =  models.CharField(max_length=255,null=True,blank=True)


    class Meta:
        managed = True
        db_table = 'employee_master'

