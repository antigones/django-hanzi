# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hanzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hanzi', models.CharField(max_length=100)),
                ('translation', models.TextField()),
                ('pinyin', models.CharField(max_length=4)),
                ('pinyin_number_notation', models.CharField(max_length=5)),
                ('stroke_count', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Radical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radical', models.CharField(max_length=1)),
                ('translation', models.TextField()),
                ('pinyin', models.CharField(max_length=4)),
                ('pinyin_number_notation', models.CharField(max_length=5)),
                ('stroke_count', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hanzi',
            name='radicals',
            field=models.ManyToManyField(to='hanzi.Radical'),
        ),
    ]
