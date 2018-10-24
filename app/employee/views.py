from rest_framework.views import APIView
from app.employee.serializers import EmployeeSerializer
from app.lib.response import ApiResponse
from app.employee.models import Employee

class EmployeeApi(APIView):

    def post(self,request):
        """
           This api create new employee.
           url: employee/create

        """
        try:
            employee_data = EmployeeSerializer(data=request.data)
            if not(employee_data.is_valid()):
                return ApiResponse().error(employee_data.errors,400)
            employee_data.save()
            return ApiResponse().success(employee_data.data,200)
        except Exception as err:
            return ApiResponse().error("Error while creating project",500)


class EmployeeDetail(APIView):
    def get(self,request,employee_id=None):
        """
           Get single employee detail using employee id.
           url: employee/detail/employee_id
        """
        try:
            get_data = EmployeeSerializer(Employee.objects.get(id=employee_id))
            return ApiResponse().success(get_data.data, 200)
        except Exception as err: 
            print(err) 
            return ApiResponse().error("please provide valid project id", 400)

class EmployeeList(APIView):
    def get(self,request):
        """
           Get all employees detail.
           url: employee/list
        """
        try: 
            emplyee_data = Employee.objects.all()
            get_data = EmployeeSerializer(emplyee_data, many=True)
            return ApiResponse().success(get_data.data, 200)
        except Exception as err: 
            print(err) 
            return ApiResponse().error("Error while getting the employee list", 400)

class EmployeeEdit(APIView):
    def put(self,request,employee_id):
        """
           This api Update employee details.
           url: employee/edit/employee_id
        """
        try:
            get_data = Employee.objects.get(pk=employee_id)
            employee_data = EmployeeSerializer(get_data,data=request.data)
            if not(employee_data.is_valid()):
                return ApiResponse().error("Error while update employee details",400)
            employee_data.save()
            return ApiResponse().success(employee_data.data,200)
        except Exception as err:
            print(err)
            return ApiResponse().success("Error",500)


# class EmployeeDisable(APIView):

#     def delete(self,request,employee_id):
#         """
#            This api make employee disable
#            url: employee/disable/employee_id 
#         """
#         try:
#             employee = Employee.objects.filter(id = employee_id,is_deleted=False).update(is_deleted=True)
#             if(employee)==0:
#                return ApiResponse().success("Employee not exists", 200) 
#             return ApiResponse().success("Employee deleted successfully", 200)
#         except Exception as err:
#             print(err)
#             return ApiResponse().error("Please send valid employee id", 400)
