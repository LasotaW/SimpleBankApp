from django.db import models
from django.utils import timezone
import datetime

class Person(models.Model):
    Imię = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=50)
    join_date = models.DateField('Data dołączenia', default=datetime.date.today)

    def __str__(self):
        return 'Klient: ' + self.Imię + ' ' + self.Nazwisko

    contactType = models.TextChoices('Typ kontaktu','ZNAJOMY RODZINA INTERNET')
    TypKontaktu = models.CharField(blank=True, choices=contactType.choices, max_length=50)

    stat = models.TextChoices('Status klienta','NOWY ZAINTERESOWANY NIEZAINTERESOWANY ZAWIESZONY')
    Status = models.CharField(blank=True, choices=stat.choices, max_length=50)

#class ContactType(models.Model):
   # Osoba = models.ForeignKey(Person, on_delete=models.CASCADE)
    
