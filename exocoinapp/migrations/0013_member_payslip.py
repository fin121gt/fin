# Generated by Django 3.2.1 on 2021-09-18 14:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exocoinapp', '0012_auto_20210918_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='payslip',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='payslip'),
        ),
    ]
