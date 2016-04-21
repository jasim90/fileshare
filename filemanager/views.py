from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from forms import FileUploadForm
from models import Files
from fileshare.common.utils import Paginate
import json
from django.core import serializers
import json

# Create your views here.


class FileUpload(View):
    template_name = "file_upload.html"
    form_class = FileUploadForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.created_by = request.user
            file.save()
            messages.success(request, 'File Uploaded...')
            return HttpResponseRedirect('/files/upload/')
        return render(request, self.template_name, {'form': form})


class MyFiles(View):
    template_name = "my_files.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        relations_to_serialize = {
            'created_by': ''
        }
        posts_value = json.loads(request.body)
        # per_page = request.POST['per_page']
        # page_no = request.POST['page_no']
        files = Paginate().paginate(Files, posts_value['params']['page_no'], posts_value['params']['per_page'])
        serializer_class = json.loads(serializers.serialize(
            "json", files['result']))
        response = {
            'result': serializer_class,
            'next': files['next'],
            'previous': files['previous'],
            'total_page': files['total_page'],
            'cur_page': files['cur_page'],
            'per_page': files['per_page']
        }
        print "???????????????????????????????", json.dumps(serializer_class)
        response_http = HttpResponse()
        response_http.status_code = 200
        response_http.write(json.dumps(response))
        response_http['Content-Type'] = 'application/json'
        return response_http
