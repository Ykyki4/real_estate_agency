# Generated by Django 2.2.24 on 2022-10-13 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20221012_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
