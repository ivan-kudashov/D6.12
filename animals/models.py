from django.db import models


import uuid



class AbstractAnimal(models.Model):

    # class Meta:
    #     abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    species = models.CharField(max_length=128)
    breed = models.CharField(max_length=64, blank=True)
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return f'{self.species} {self.name}'



class Cat(AbstractAnimal):

    color = models.CharField(max_length=32)

    FUR_CHOICE = (
        ('L', 'Long'),
        ('S', 'Short'),
        ('H', 'Hairless')
    )
    fur = models.CharField(max_length=1, choices=FUR_CHOICE, default='S')


class Dog(AbstractAnimal):

    SIZE_CHOICE = (
        ('L', 'Large'),
        ('M', 'Medium'),
        ('S', 'Small'),
    )
    size = models.CharField(max_length=1, choices=SIZE_CHOICE, default='M')
