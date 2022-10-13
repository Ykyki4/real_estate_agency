# Generated by Django 2.2.24 on 2022-10-12 11:50

from django.db import migrations


def add_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(add_owners)
    ]

