# Generated by Django 4.0.5 on 2022-06-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0021_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='choice',
            field=models.CharField(default='Yes', max_length=3),
        ),
    ]