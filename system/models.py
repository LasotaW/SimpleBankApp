from django.db import models
from django.utils import timezone
import datetime

class Klienci(models.Model):
    Imię = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=50)
    join_date = models.DateField('Data dołączenia', default=datetime.date.today)
    
    class Meta:                        #Niweluje dodawanie "s" na końcu wyrazu/Removes extra "s" from classes
        verbose_name_plural = "Klienci"

    def __str__(self):
        return self.Imię + ' ' + self.Nazwisko

    contactType = models.TextChoices('Typ kontaktu','ZNAJOMY RODZINA INTERNET')
    Contact = models.CharField('Typ kontaktu', blank=True, choices=contactType.choices, max_length=50)

    stat = models.TextChoices('Status klienta','NOWY ZAINTERESOWANY NIEZAINTERESOWANY ZAWIESZONY')
    Status = models.CharField('Status klienta', blank=True, choices=stat.choices, max_length=50)
