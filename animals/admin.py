from django.contrib import admin

from animals.models import Cat, Dog
from .forms import CatAdminForm, DogAdminForm



@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):

    form = CatAdminForm


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):

    form = DogAdminForm



