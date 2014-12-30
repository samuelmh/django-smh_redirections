# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Redirection',
            fields=[
                ('id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('alias', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('public', models.BooleanField(default=False)),
                ('last_refresh', models.DateTimeField(auto_now=True)),
                ('prints', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
