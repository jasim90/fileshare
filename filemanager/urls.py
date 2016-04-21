from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from views import FileUpload, MyFiles
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^upload/$', login_required(FileUpload.as_view()), name="file_upload"),
    url(r'^myfiles/$', csrf_exempt(login_required(MyFiles.as_view())), name="my_files"),

]
