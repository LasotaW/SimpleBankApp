from django.contrib import admin

from .models import Klienci

class Columns(admin.ModelAdmin):
   list_display = ('Imię', 'Nazwisko','join_date', 'Contact', 'Status')

admin.site.register(Klienci, Columns)