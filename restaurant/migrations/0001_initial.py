# Generated by Django 4.2 on 2023-04-30 04:16

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=2048)),
                ('address', models.CharField(max_length=1024)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('active', 'Active')], default='pending', max_length=64)),
                ('menu', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='management.city')),
                ('cuisines', models.ManyToManyField(related_name='restaurants', to='management.cuisine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('seats', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='restaurant.restaurant')),
            ],
        ),
    ]
