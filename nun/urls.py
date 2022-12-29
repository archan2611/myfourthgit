from django.urls import path
from nun.views import *
app_name='somethings'

urlpatterns=[
    path('jinja1/',jinja1,name='jina1'),
]