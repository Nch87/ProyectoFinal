# Generated by Django 4.2.5 on 2023-09-14 14:24

import AppInicio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcion',
            name='imagen',
            field=models.ImageField(upload_to=AppInicio.models.image_upload_path),
        ),
    ]
