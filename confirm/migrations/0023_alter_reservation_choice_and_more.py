# Generated by Django 4.0.5 on 2022-06-24 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0022_reservation_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='choice',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
