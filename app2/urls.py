from django.urls import path
from app2.views import *

app_name='dhoni'

urlpatterns=[
    path('sahana/',sahana,name='sahana'),
]
