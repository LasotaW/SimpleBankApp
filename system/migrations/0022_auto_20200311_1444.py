# Generated by Django 3.0.4 on 2020-03-11 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0021_auto_20200311_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacttype',
            old_name='person',
            new_name='Osoba',
        ),
    ]
