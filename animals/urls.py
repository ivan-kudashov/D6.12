from django.urls import path
from .views import CatList, CatDetail, DogList, DogDetail, search


app_name = 'animals'
urlpatterns = [
    path('cats/', CatList.as_view(), name='cat_list'),
    path('cat/<str:pk>', CatDetail.as_view(), name='cat_detail'),
    path('dogs/', DogList.as_view(), name='dog_list'),
    path('dog/<str:pk>', DogDetail.as_view(), name='dog_detail'),
    path('search/', search)
]
