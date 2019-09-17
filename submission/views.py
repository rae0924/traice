from django.shortcuts import render
from django.views.generic import TemplateView
import json


# Create your views here.
class SubmissionView(TemplateView):

    template_name = 'submission/submission.html'

    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        print("hello")
        data = request.POST['data']
        data = json.load(data)
        print(data)
        return render(request, self.template_name)