from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import MainPage


class MainPageForm(forms.ModelForm):

    class Meta:
        model = MainPage
        fields = '__all__'

    phone_number = PhoneNumberField()
