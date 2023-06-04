# Generated by Django 4.0.6 on 2023-05-16 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('balance', models.FloatField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=225)),
                ('logo', models.ImageField(upload_to='logo,')),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_acct', models.CharField(blank=True, max_length=15, null=True)),
                ('w_address', models.CharField(blank=True, max_length=225, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
