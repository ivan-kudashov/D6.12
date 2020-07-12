from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class MainPage(models.Model):
    title = models.CharField(max_length=128)
    page_text = models.TextField()

    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=128)
    location = models.TextField()
