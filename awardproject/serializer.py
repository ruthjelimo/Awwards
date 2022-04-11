from rest_framework import serializers
from .models import Profile,Project,User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =('profile_photo','bio','contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = ('image','title','description','url')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username','email')