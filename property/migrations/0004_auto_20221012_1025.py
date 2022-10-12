# Generated by Django 2.2.24 on 2022-10-12 07:25

from django.db import migrations

def add_value_to_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    new_building_flats = Flat.objects.filter(construction_year__gte=2015)
    old_building_flats = Flat.objects.filter(construction_year__lte=2014)
    for new_building_flat in new_building_flats:
        new_building_flat.new_building = True
        new_building_flat.save()
    for old_building_flat in old_building_flats:
        old_building_flat.new_building = False
        old_building_flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(add_value_to_new_building)
    ]