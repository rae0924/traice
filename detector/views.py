from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from detector.models import UserTrial
from binascii import a2b_base64
from django.conf import settings
import cv2
import os
# Create your views here.

class DetectorView(TemplateView):
    
    template_name = 'detector/detector.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        dataURL = request.POST['data']
        _, data = dataURL.split(",", 1)
        binary_data = a2b_base64(data)
        return render(request, 'detector/detector.html')
    