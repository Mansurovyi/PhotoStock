# Generated by Django 4.2.6 on 2023-12-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='discription',
            new_name='description',
        ),
    ]