from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from infopages.models import MainPage


def index(request):
    template = loader.get_template('index.html')
    main_page = MainPage.objects.first()
    data = {'content': main_page, 'HomeActive': 'active'}
    return HttpResponse(template.render(data, request))
