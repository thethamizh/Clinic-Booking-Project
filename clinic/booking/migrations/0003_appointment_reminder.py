# Generated by Django 5.0.6 on 2024-05-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_appointment_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='reminder',
            field=models.BooleanField(default=True),
        ),
    ]
