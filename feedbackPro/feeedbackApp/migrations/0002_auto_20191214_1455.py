# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-12-14 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeedbackApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdata',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
