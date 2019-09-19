from django.db import models

class Sample(models.Model):

    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=30, default='')
    label = models.IntegerField(default=0)
    img_path = models.FilePathField(default='')

    def __str__(self):
        return self.img_path[15:]
# Create your models here.
