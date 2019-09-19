from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
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
            'is_repeat': False,
            'invalid_email': False,
            'success': True,
        }

        with open('home/static/home/blank.json', 'r') as f:
            blank = json.load(f) 

        if data['dataurl'] == blank['blank_canvas']:
            args['has_empty_field'] = True
            args['success'] = False
            return render(request, self.template_name, args)
        
        if not data['first_name'] or not data['last_name'] or not data['email']:
            args['has_empty_field'] = True
            args['success'] = False
            return render(request, self.template_name, args)

        try:
            validate_email(data['email'])
            
        except ValidationError:
            args['invalid_email'] = True
            args['success'] = False
            return render(request, self.template_name, args)


        for sample in Sample.objects.filter(email=data['email']).all():
            if int(data['label']) == sample.label:
                args['is_repeat'] = True
                image_path = sample.img_path[1:]
                with open(image_path, 'wb') as f:
                    f.write(a2b_base64(data['dataurl']))
                return render(request, self.template_name, args)

        sample = Sample(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            label = data['label']
        )

        sample.save()
        image_data = a2b_base64(data['dataurl'])
        default_path = 'media/samples/'
        image_name = 'sample_' + str(sample.pk) + '.png'
        image_path = os.path.join(default_path, image_name)
        sample.img_path = '/' + image_path 
        with open(image_path, 'wb') as f:
            f.write(image_data)
        sample.save()
        return render(request, self.template_name, args)