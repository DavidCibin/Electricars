# Generated by Django 3.2.2 on 2021-05-13 00:19

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20210512_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='insurance',
            field=models.CharField(choices=[('N', 'No Coverage'), ('F', 'Full Coverage (+$20.00/day)')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]
