# Generated by Django 4.0.6 on 2023-05-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='commision',
            field=models.IntegerField(default=3),
        ),
    ]
