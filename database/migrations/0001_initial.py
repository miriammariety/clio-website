# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import database.models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cover', models.ImageField(upload_to=b'album_covers')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(default=database.models.generate_profile_slug, unique=True, max_length=15, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[\\w-]{5,15}$', message=b'Vanity url must be at least 5 characters, most 15 characters')])),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photos')),
                ('album', models.ForeignKey(related_name='photos', to='database.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('shipping_address', models.TextField(blank=True)),
                ('payable', models.IntegerField(default=0)),
                ('mode', models.IntegerField(choices=[(1, b'Delivery'), (2, b'Pick Up')])),
                ('client', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
