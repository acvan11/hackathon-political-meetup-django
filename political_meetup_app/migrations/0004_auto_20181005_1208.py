# Generated by Django 2.1.1 on 2018-10-05 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('political_meetup_app', '0003_venue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
