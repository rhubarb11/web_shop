# Generated by Django 3.1.1 on 2020-09-15 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20200911_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
