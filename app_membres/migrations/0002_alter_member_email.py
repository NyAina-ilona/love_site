# Generated by Django 5.0.6 on 2025-03-13 12:41

import app_membres.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_membres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[app_membres.models.validate_email]),
        ),
    ]
