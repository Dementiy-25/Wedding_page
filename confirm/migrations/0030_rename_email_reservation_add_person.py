# Generated by Django 4.0.5 on 2022-07-03 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0029_alter_reservation_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='email',
            new_name='add_person',
        ),
    ]
