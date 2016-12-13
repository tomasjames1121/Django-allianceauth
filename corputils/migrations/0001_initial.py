# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-13 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('esi', '0002_scopes_20161208'),
        ('eveonline', '0004_eveapikeypair_sso_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorpStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('_members', models.TextField(default='{}')),
                ('corp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eveonline.EveCorporationInfo')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esi.Token')),
            ],
            options={
                'default_permissions': ('add', 'delete', 'view'),
                'permissions': (('corp_apis', 'Can view API keys of members of their corporation.'), ('alliance_apis', 'Can view API keys of members of their alliance.'), ('blue_apis', 'Can view API keys of members of blue corporations.')),
            },
        ),
    ]
