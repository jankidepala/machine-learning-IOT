from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=101)
    submitter = models.CharField(max_length=101)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=101)
    submission_date = models.DateTimeField()
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)


