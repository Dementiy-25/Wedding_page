# Generated by Django 4.0.5 on 2022-06-20 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0012_alter_wedding_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wedding',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='confirm.country'),
        ),
    ]