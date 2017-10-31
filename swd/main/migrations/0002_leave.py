# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTimeStart', models.DateTimeField()),
                ('dataTimeEnd', models.DateTimeField()),
                ('reason', models.TextField()),
                ('consent', models.CharField(max_length=10)),
                ('corrAddress', models.TextField()),
                ('corrPhone', models.CharField(max_length=15)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student')),
            ],
        ),
    ]