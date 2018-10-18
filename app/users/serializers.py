from rest_framework import serializers
from app.users.models import UserProfile
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','email','password')
        extra_kwargs = {
            
            'email': {
                'required':True,
                'error_messages':{
                'required':"Email field is required"
                }
            },
            
        }
        

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id','user','first_name','last_name','is_deleted','created_at','updated_at','status')
        extra_kwargs = {
           
            'email': {
                'required':True,
                'error_messages':{
                'required':"This field is required"
                }
            },
            
        }