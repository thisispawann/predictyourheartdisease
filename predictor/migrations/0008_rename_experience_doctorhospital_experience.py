# Generated by Django 4.0 on 2022-01-02 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0007_rename_location_doctorhospital_experience_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorhospital',
            old_name='Experience',
            new_name='experience',
        ),
    ]
