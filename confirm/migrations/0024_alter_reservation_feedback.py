# Generated by Django 4.0.5 on 2022-06-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0023_alter_reservation_choice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='feedback',
            field=models.TextField(blank=''),
        ),
    ]