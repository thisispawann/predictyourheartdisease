# Generated by Django 4.0 on 2022-01-02 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0008_rename_experience_doctorhospital_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctorhospital',
            options={'ordering': ('experience',)},
        ),
    ]
