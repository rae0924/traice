from django.db import models

class Sample(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_sample = models.BooleanField(default=False)
    label = models.IntegerField(default=10)
    img_path = models.FilePathField(default='')

# Create your models here.
