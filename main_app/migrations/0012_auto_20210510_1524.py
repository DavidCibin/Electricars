# Generated by Django 3.2.2 on 2021-05-10 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_profile_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Address1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Address2',
            new_name='address2',
        ),
    ]