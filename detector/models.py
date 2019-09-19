from django.db import models

# Create your models here.

class UserTrial(models.Model):

    detector_prediction = models.IntegerField(default=0)
    img_path = models.FilePathField(default='')

    def __str__(self):
        return self.img_path[14:]