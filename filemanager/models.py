from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.


class Files(models.Model):
    file_name = models.CharField(
        max_length=30,
        validators=[
            validators.RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='File name must be alphanumeric',
                code='invalid_file_name'
            ),
        ],
        unique=True
    )
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    file_type = models.IntegerField(null=True)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class SharedFiles(models.Model):
	file = models.ForeignKey(Files)
	shared_by = models.ForeignKey(User, related_name="shared_from")
	shared_to = models.ForeignKey(User, related_name="shared_to")
	shared_on = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)