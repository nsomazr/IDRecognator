from django.db import models
# Create your models here.
import os
from os.path import dirname, join, abspath
__dir__ = dirname(abspath(__file__))
UPLOAD_ROOT = join(__dir__, 'filepaths')
from django.utils import timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))

class ImageModel(models.Model):
    filepaths = models.FileField(max_length=200,upload_to=os.path.join(BASE_DIR,'IDRecApp/static/filepaths/'))
    filename = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    upload_date = models.DateTimeField(default=timezone.now)


class DataModel(models.Model):
    user_id = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    forenames = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    date_issued = models.CharField(max_length=100)
    id_no = models.CharField(max_length=100)
    upload_date = models.DateTimeField(default=timezone.now)
