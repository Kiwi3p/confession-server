from django.contrib.auth.models import User, Group
from quickstart.models import DRFPost 
from quickstart.models import Questions 
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DRFPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = DRFPost
		fields = '__all__'    

class QuestionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Questions
		fields = '__all__'               