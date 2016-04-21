from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

from filemanager.models import Files, SharedFiles
from utils import paginate
# Create your views here.

class UserViewSet(APIView):
	def post(self, request, format=None):
	    queryset = User.objects.all()
	    page = request.data.get('page')
	    pagination = paginate(queryset, page, 10)
	    serializer_class = UserSerializer(pagination['objects'], many=True)
	    response = {
	    	'result': serializer_class.data,
	    	'next': pagination['next_page'],
	    	'previous': pagination['prev_page'],
	    	'total_page': pagination['total_page']
	    }
	    return Response(response)

class FileViewSet(APIView):
	def get(self, request, format=None):
		queryset = Files.objects.all()
		page = request.data.get('page')
		pagination = paginate(queryset, page, 10)
		serializer_class = FilesSerializer(pagination['objects'], many=True)
		response = {
	    	'result': serializer_class.data,
	    	'next': pagination['next_page'],
	    	'previous': pagination['prev_page'],
	    	'total_page': pagination['total_page']
	    }
		return Response(response)

class SharedFileViewSet(APIView):
	def get(self, request, format=None):
		queryset = SharedFiles.objects.all()
		page = request.data.get('page')
		pagination = paginate(queryset, page, 10)
		serializer_class = SharedFilesSerializer(pagination['objects'], many=True)
		response = {
			'result': serializer_class.data,
			'next': pagination['next_page'],
			'previous': pagination['prev_page'],
			'total_page': pagination['total_page']
		}
		return Response(response)