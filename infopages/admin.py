from django.contrib import admin
from .models import MainPage
from .forms import MainPageForm


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    form = MainPageForm
