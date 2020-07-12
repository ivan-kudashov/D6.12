from django.urls import path
from .views import index


app_name = 'infopages'
urlpatterns = [
    path('', index),
    path('index/', index),
]
