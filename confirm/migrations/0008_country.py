# Generated by Django 4.0.5 on 2022-06-19 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0007_rename_years_wedding_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, default='Ireland', max_length=80)),
            ],
        ),
    ]
