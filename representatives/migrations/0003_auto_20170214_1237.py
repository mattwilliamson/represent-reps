# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-14 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('representatives', '0002_auto_20141129_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='extra',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='offices',
            field=jsonfield.fields.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='election',
            name='data_url',
            field=models.URLField(help_text='URL to a JSON array of individuals within this set'),
        ),
        migrations.AlterField(
            model_name='election',
            name='name',
            field=models.CharField(help_text='The name of the political body, e.g. House of Commons', max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='representative',
            name='extra',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='representative',
            name='offices',
            field=jsonfield.fields.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='representativeset',
            name='data_url',
            field=models.URLField(help_text='URL to a JSON array of individuals within this set'),
        ),
        migrations.AlterField(
            model_name='representativeset',
            name='name',
            field=models.CharField(help_text='The name of the political body, e.g. House of Commons', max_length=300, unique=True),
        ),
    ]
