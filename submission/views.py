from django.shortcuts import render
from django.views.generic import TemplateView
from submission.models import Sample
import json


# Create your views here.
class SubmissionView(TemplateView):

    template_name = 'submission/submission.html'

    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        data = json.loads(request.POST['data'])
        _, data['dataurl'] = data['dataurl'].split(",", 1)
        return render(request, self.template_name)