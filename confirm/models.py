from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.country


class Wedding(models.Model):
    Gender_CHOICES = [
        ('m', 'male'),
        ('f', 'female'),
       ]

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    gender = models.CharField(max_length=1, choices=Gender_CHOICES,default='m')
    slug = models.SlugField(default='', null=False, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)

    def save(self, *args, **kwargs):
        slug_name = self.first_name + '-' + self.last_name
        self.slug = slugify(slug_name)
        super(Wedding, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('guest_detail', args=[self.slug])

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.age}, {self.gender}'

class Reservation(models.Model):
    CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    choice = models.CharField(max_length=3, choices=CHOICES, default='Yes')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    add_person = models.CharField(max_length=100, blank=True, default=None)
    feedback = models.TextField(blank=True, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'