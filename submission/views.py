from django.shortcuts import render
from django.views.generic import TemplateView
from submission.models import Sample
from binascii import a2b_base64
import json, os


# Create your views here.
class SubmissionView(TemplateView):

    template_name = 'submission/submission.html'

    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        data = json.loads(request.POST['data'])
        _, data['dataurl'] = data['dataurl'].split(",", 1)

        args = {
            'data': data,
            'has_empty_field': False,
            'canvas_blank': False,
            'repeat': False,
        }

        if not data['first_name'] or not data['last_name'] or not data['email']:
            args['has_empty_field'] = True
            return render(request, self.template_name, args)
        
        for sample in Sample.objects.filter(is_sample=True).all():
            if data['email'] == sample.email & data['digit'] == sample.label:
                args['repeat'] = True
                return render(request, self.template_name, args)

        sample = Sample(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            is_sample = True,
            label = data['digit']
        )
        sample.save()
        image_data = a2b_base64(data)
        default_path = 'media/samples/'
        image_name = str(sample.pk) + '.png'
        image_path = os.path.join(default_path, image_name)
        sample.img_path = '/' + image_path 
        with open(image_path, 'wb') as f:
            f.write(image_data)
        sample.save()
        return render(request, self.template_name, args)