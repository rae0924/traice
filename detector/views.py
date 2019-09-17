from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from submission.models import Sample
from binascii import a2b_base64
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
        default_path = 'media/samples/'
        sample = Sample()
        sample.save()
        img_name = str(sample.pk) + '.png'
        img_path = os.path.join(default_path, img_name)
        sample.img_path = '/' + img_path
        sample.save()
        with open(img_path, 'wb') as f:
            f.write(binary_data)
        # image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        # trans_mask = image[:,:,3] == 0
        # image[trans_mask] = [255, 255, 255, 255]
        args = {'sample': sample}
        return render(request, 'detector/summary.html', args)
        
    
        