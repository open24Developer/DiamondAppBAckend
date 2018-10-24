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
    email = serializers.SerializerMethodField("getEmail")
    def getEmail(self,obj):
        try:
            return User.objects.get(id=obj.user.id).email
        except Exception as e:
            print(e)

    class Meta:
        model = UserProfile
        fields = ('id','user','first_name','last_name','email','is_deleted','created_at','updated_at','status')
        extra_kwargs = {
           
            'email': {
                'required':True,
                'error_messages':{
                'required':"This field is required"
                }
            },
            
        }