from rest_framework import serializers
from app.employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'employee_id','first_name','middle_name','last_name','prior_last_name', \
        		'suffix','address_1','address_2','city','state','zip_code','country','disability', \
        		'ethnicity','gender','smoker','veteran','birth_date','employee_status_effective_date', \
        		'employee_status','hire_date','rehire_date','termination_date', \
        		'user_account_deactivation_date','annual_salary','cost_code','department', \
        		'division','eeo_class','employment_type','is_supervisor_reviewer', \
        		'job_title','position')
        