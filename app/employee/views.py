from rest_framework.views import APIView
from app.employee.serializers import EmployeeSerializer
from app.lib.response import ApiResponse
from app.employee.models import Employee

class EmployeeApi(APIView):

    def post(self,request):
        """
           This api create new employee.
           url: employee/create
           required field: employee(string),system_of_origin(string),project_status(string),database_stamp(string)
        """
        try:
            project_data = EmployeeSerializer(data=request.data)
            if not(project_data.is_valid()):
                return ApiResponse().error(project_data.errors,400)
            project_data.save()
            return ApiResponse().success(project_data.data,200)
        except Exception as err:
            return ApiResponse().error("Error while creating project",500)


    def get(self,request,employee_id=None):
        """
           Get single employee detail using employee id.
           url: employee/detail/employee_id
           Get all employees detail.
           url: employee/list
        """
        try:
            if(employee_id):
                try:
                    get_data = EmployeeSerializer(Employee.objects.get(id=employee_id))
                except Exception as err:
                    print(err)  
                    return ApiResponse().error("please provide valid project id", 400)
            else:
                emplyee_data = Employee.objects.all()
                get_data = EmployeeSerializer(emplyee_data, many=True)
            return ApiResponse().success(get_data.data, 200)
        except Exception as err: 
            print(err) 
            return ApiResponse().error("Error while getting the project details", 500)


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

    # def delete(self,request,project_id):
    #     """
    #        This api make project disable
    #        url: project/disable/project_id 
    #     """
    #     try:
    #         project = Project.objects.filter(id = project_id,is_deleted=False).update(is_deleted=True)
    #         if(project)==0:
    #            return ApiResponse().success("Project not exists", 200) 
    #         return ApiResponse().success("Project deleted successfully", 200)
    #     except Exception as err:
    #         print(err)
    #         return ApiResponse().error("Please send valid project id", 400)