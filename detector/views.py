from django.shortcuts import render

# Create your views here.

def detector(request):
    return render(request, 'detector/detector.html')