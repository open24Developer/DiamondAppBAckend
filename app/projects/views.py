from rest_framework.views import APIView
from app.projects.serializers import ProjectSerializer
from app.lib.response import ApiResponse
from app.projects.models import Project


class ProjectApi(APIView):

    def post(self,request):
        """
           This api create new project.
           url: project/create
           required field: project(string),system_of_origin(string),project_status(string),database_stamp(string)
        """
        try:
            project_data = ProjectSerializer(data=request.data)
            if not(project_data.is_valid()):
                return ApiResponse().error(project_data.errors,400)
            project_data.save()
            return ApiResponse().success(project_data.data,200)
        except Exception as err:
            return ApiResponse().error("Error while creating project",500)


class ProjectDeatil(APIView):

    def get(self,request,project_id=None):
        """
           Get single project detail using project id.
           url: project/detail/project_id

        """
        try:
            get_data = ProjectSerializer(Project.objects.get(is_deleted=False, id=project_id))
            return ApiResponse().success(get_data.data, 200)
        except Exception as err: 
            print(err) 
            return ApiResponse().error("please provide valid project id", 400)

class ProjectList(APIView):

    def get(self,request):
        """
           Get all project detail.
           url: project/list
        """
        try:
            project_data = Project.objects.filter(is_deleted=False)
            get_data = ProjectSerializer(project_data, many=True)
            # pagination_class = ProjectPagination(get_data)
            return ApiResponse().success(get_data.data, 200)
        except Exception as err: 
            print(err) 
            return ApiResponse().error("Error while getting the project details", 500)

class ProjectEdit(APIView):

    def put(self,request,project_id):
        """
           This api Update project details.
           url: project/edit/project_id
        """
        try:
            get_data = Project.objects.get(pk=project_id)
            project_data = ProjectSerializer(get_data,data=request.data)
            if not(project_data.is_valid()):
                return ApiResponse().error("Error while update project details",400)
            project_data.save()
            return ApiResponse().success(project_data.data,200)
        except Exception as err:
            print(err)
            return ApiResponse().success("Error",500)

class ProjectDisable(APIView):

    def delete(self,request,project_id):
        """
           This api make project disable
           url: project/disable/project_id 
        """
        try:
            project = Project.objects.filter(id = project_id,is_deleted=False).update(is_deleted=True)
            if(project)==0:
               return ApiResponse().success("Project not exists", 200) 
            return ApiResponse().success("Project deleted successfully", 200)
        except Exception as err:
            print(err)
            return ApiResponse().error("Please send valid project id", 400)