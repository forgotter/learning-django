from django.urls import path
from .models import *
from .views import *

app_name = 'exam'

urlpatterns = [
    path('ViewTest',CreateTest, name='CreateTest'),
    path('SubmitTest', SubmitTest, name='SubmitTest'),
    path('Feedback', Feedback, name='Feedback'),
    path('TestOver', TestOver, name='TestOver'),
]