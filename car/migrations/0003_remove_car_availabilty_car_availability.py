# Generated by Django 4.2.2 on 2023-06-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_reservation_delete_reservarion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='availabilty',
        ),
        migrations.AddField(
            model_name='car',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
