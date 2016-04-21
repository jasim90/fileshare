from rest_framework import serializers
from django.contrib.auth.models import User
from filemanager.models import Files, SharedFiles
# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')

class FilesSerializer(serializers.ModelSerializer):

	created_by = UserSerializer()

	class Meta:
		model = Files
		fields = ('id','file_name', 'file', 'file_type', 'created_by', 'created_on')

class SharedFilesSerializer(serializers.ModelSerializer):

	file = FilesSerializer()
	shared_by = UserSerializer()
	shared_to = UserSerializer()

	class Meta:
		model = SharedFiles
		fields = ('id','file', 'shared_by', 'shared_to', 'shared_on', 'status')