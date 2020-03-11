from django.db import models
from django.utils import timezone
import datetime

class Person(models.Model):
    Imię = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=50)
    join_date = models.DateField('Data dołączenia', default=datetime.date.today)

class ContactType(models.Model):
    znajomy = models.ForeignKey('Person', on_delete=models.CASCADE)
