from django.db import models

# Create your models here.

year_choices = [(y, y) for y in range(1990, 2026)]
fuel_choices = [(x, x) for x in ('Diesel', 'Benzina', 'GPL', 'Hybrid', 'Benzina + GPL')]
gear_choices = [(x, x) for x in ('Manual', 'Automat')]
transmission_choices = [(x, x) for x in ('Fata', 'Spate', '4x4')]





class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Brand')
    model = models.CharField(max_length=50, verbose_name='Model')
    year = models.CharField(max_length=20, verbose_name='Anul producerii', choices=year_choices)
    hp = models.CharField(max_length=50, verbose_name='Putere (cp)', null=True)
    kw = models.CharField(max_length=50, verbose_name='Putere (kw))', null=True)
    fuel = models.CharField(max_length=20, verbose_name='Combustibil', choices=fuel_choices)
    gearbox = models.CharField(max_length=10, verbose_name='Cutie',  choices=gear_choices)
    transmission = models.CharField(max_length=20, verbose_name='Transmisie',  choices=transmission_choices)
    color = models.CharField(max_length=20, verbose_name='Culoare')
    body = models.CharField(max_length=20, verbose_name='Caroserie')
    seats = models.CharField(max_length=50, verbose_name='Locuri')
    urban_comsumption = models.CharField(max_length=50, verbose_name='Consum oras', blank=True)
    extra_urban_comsumption = models.CharField(max_length=50, verbose_name='Consum exterior', blank=True)
    mixed_comsumption = models.CharField(max_length=50, verbose_name='Consum mixt', blank=True)
