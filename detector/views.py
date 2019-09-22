from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from detector.models import UserTrial
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
        default_path = 'media/random/'
        rand = UserTrial()
        rand.save()
        img_name = 'random_' + str(rand.pk) + '.png'
        img_path = os.path.join(default_path, img_name)
        rand.img_path = '/' + img_path
        rand.save()
        with open(img_path, 'wb') as f:
            f.write(binary_data)
        image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        trans_mask = image[:,:,3] == 0
        image[trans_mask] = [180, 120, 25, 255]
        cv2.imwrite(img_path, image)
        args = {'rand': rand}
        return render(request, 'detector/summary.html', args)
        
    
        