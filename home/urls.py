from django.urls import path
from . import views
from detector import views as detector_views

urlpatterns = [
    path('', views.home, name='home'),
    path('detector', detector_views.detector, name='detector')
]