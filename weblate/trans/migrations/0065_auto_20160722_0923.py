# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 07:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

from weblate.trans.vcs import VCS_CHOICES


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0064_auto_20160428_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='vcs',
            field=models.CharField(choices=VCS_CHOICES, default=settings.DEFAULT_VCS, help_text='Version control system to use to access your repository with translations.', max_length=20, verbose_name='Version control system'),
        ),
    ]
