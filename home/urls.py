from django.urls import path
from . import views
from detector.views import DetectorView
from submission.views import SubmissionView

urlpatterns = [
    path('', views.home, name='home'),
    path('detector/', DetectorView.as_view(), name='detector'),
    path('submission/', SubmissionView.as_view(), name='submission'),
    path('about/', views.about, name='about')
]
