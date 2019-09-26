from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path ('',views.home, name = 'WeDoCal'),
    path('signein/',views.register,name='register'),
    path('check/',views.consult,name='check'),
    path('dose/<int:pk>',views.dose_create,name='dose-create'),

]
