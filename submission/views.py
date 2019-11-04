from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from submission.models import Sample
from binascii import a2b_base64
import json, os, boto3
from django.conf import settings


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

        try:
            with open('./static/home/blank.json', 'r') as f:
                blank = json.load(f) 
        except:
            with open('/home/ubuntu/trAIce/static/home/blank.json', 'r') as f:
                blank = json.load(f)

        with open(settings.CONFIG_PATH) as f:
            config = json.load(f)
            ACCESS_KEY_ID = config["S3_ACCESS_KEY_ID"]
            SECRET_ACCESS_KEY = config["S3_SECRET_ACCESS_KEY"]
            BUCKET_NAME = config["S3_BUCKET_NAME"]

        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

        if data['dataurl'] == blank['blank_canvas']:
            args['has_empty_field'] = True
            args['success'] = False
            return render(request, self.template_name, args)
        
        image_data = a2b_base64(data['dataurl'])

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
                image_path = sample.img_path
                s3.put_object(Body=image_data, Bucket=BUCKET_NAME, Key=image_path)
                return render(request, self.template_name, args)

        sample = Sample(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            label = data['label']
        )

        sample.save()
        image_path = 'samples/sample_' + str(sample.pk) + '.png'
        s3.put_object(Body=image_data, Bucket=BUCKET_NAME, Key=image_path)
        sample.img_path = image_path
        sample.save()
        return render(request, self.template_name, args)
