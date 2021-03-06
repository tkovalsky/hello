# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-01 18:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0003_auto_20161201_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teammates', models.ManyToManyField(through='collection.Thing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='thing',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Team'),
        ),
    ]
