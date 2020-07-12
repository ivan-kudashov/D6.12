from django import forms
from .models import Cat, Dog





class CatAdminForm(forms.ModelForm):

    class Meta:
        model = Cat
        exclude = ('species', 'id')

    def clean(self):
        # set default species for this class
        self.instance.species = 'cat'
        return super(CatAdminForm, self).clean()


class DogAdminForm(forms.ModelForm):

    class Meta:
        model = Dog
        exclude = ('species', 'id')

    def clean(self):
        # set default species for this class
        self.instance.species = 'dog'
        return super(DogAdminForm, self).clean()
