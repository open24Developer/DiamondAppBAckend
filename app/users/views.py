from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from app.users.serializers import ProfileSerializer,UserSerializer
from app.users.models import UserProfile
from app.lib.common import RequestOverwrite
from app.lib.response import ApiResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserApi(APIView):
    
    # permission_classes = (IsAuthenticatedOrCreate, )
    def post(self,request):
        """This api use to create user.'Email' and 'Password' field is required"""
        try:
            user_info = UserSerializer(data = request.data)
            if not user_info.is_valid():
                return ApiResponse().error(user_info.errors,400)
            user = self.create_user(request)
            if not(user):
                return ApiResponse().error("This email is already exists", 400)
            RequestOverwrite().overWrite(request, {'user':user.id})
            user_data = ProfileSerializer(data=request.data)
            if not(user_data.is_valid()):
                return ApiResponse().error(user_data.errors, 400)
            user_data.save()
            return ApiResponse().success(user_data.data, 200)
        except Exception as err:
            print(err)
            return ApiResponse().error("There is a problem while creating user", 500)

    def create_user(self,request):
        try:
            user = User.objects.create_user(username=request.data.get('email'),
            email=request.data.get('email'),password=request.data.get('password'),is_staff=True)
            return user
        except Exception as err:
            print(err)
            return None

    def put(self,request,user_id):
        try:
            """This api use to update user details """
            if(request.data.get('email')):
                try:
                    user = User.objects.get(email=request.data.get('email'))
                    if int(user_id) != int(user.id):
                        return ApiResponse().error("This email is already exists", 400)
                except Exception as err:
                    print(err)
                get_data = UserProfile.objects.get(user=user_id)
                RequestOverwrite().overWrite(request, {'user':user_id})
                User.objects.filter(id = user_id).update(email = request.data.get('email'), username = request.data.get('email'))
                update_data = ProfileSerializer(get_data,data=request.data)
                if update_data.is_valid():
                    update_data.save()
                    return ApiResponse().success(update_data.data, 200)
                else:
                    return ApiResponse().error(update_data.errors, 400) 
        except Exception as err:
            print(err)
            return ApiResponse().error("Error", 500)

    def delete(self,request,user_id):
        try:
            """This api use to make user disable"""
            import random,string
            email_val = User.objects.get(id=user_id).email
            random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
            usrename = random + "@gmail.com"
            email = random + "@gmail.com"
            User.objects.filter(id = user_id).update(username = usrename,email= email,is_active=False)
            UserProfile.objects.filter(user=user_id).update(is_deleted=True,deleted_val = email_val)
            return ApiResponse().success("User disabled", 200)
        except Exception as err:
            print(err)
            return ApiResponse().error("Please send valid id", 500)


class LoginApi(APIView):
    
    
    def post(self,request):
        try:
            if request.data.get('email') and request.data.get('password'):
                user = UserSerializer(data = request.data)
                if not user.is_valid():
                    return ApiResponse().error(user.errors,400)
                try:
                    user_email = User.objects.get(email=request.data.get('email'))
                    auth_user = authenticate(username=user_email,password=request.data.get('password'))
                except Exception as err:
                    print(err)
                    return ApiResponse().error("Invalid username or password", 400)     
                if not auth_user:
                    return ApiResponse().error("invalid username or password", 400) 
                token,create = Token.objects.get_or_create(user_id=auth_user.id)    
                if(auth_user):
                    try:
                        userprofile = UserProfile.objects.get(user_id=auth_user.id, is_deleted=False)
                        user_data = ProfileSerializer(userprofile)
                    except Exception as err:
                        print(err)  
                        return ApiResponse().error("invalid email or password", 400)

                token_value = {
                    'token':token.key,
                    }
                user_response = user_data.data
                user_response.update(token_value)
                return ApiResponse().success(user_response, 200)
            return ApiResponse().error("Please send correct email and password", 400)
        except Exception as err:
            print(err)
            return ApiResponse().error("Error while login", 500)
