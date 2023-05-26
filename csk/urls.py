from django.urls import path
from csk.views import *
app_name='anything'
urlpatterns=[
    path('MSD/',MSD,name='MSD')
]