from django.db import models

class Sample(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=30, default='')
    is_sample = models.BooleanField(default=False)
    label = models.IntegerField(default=0)
    img_path = models.FilePathField(default='')

# Create your models here.
