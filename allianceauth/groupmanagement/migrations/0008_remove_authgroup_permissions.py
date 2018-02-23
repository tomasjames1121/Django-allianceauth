# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 23:09
from __future__ import unicode_literals

from django.db import migrations


def delete_permissions(apps, schema_editor):
    AuthGroup = apps.get_model('groupmanagement', 'AuthGroup')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    ct = ContentType.objects.get_for_model(AuthGroup)
    Permission.objects.filter(content_type=ct).delete()


def recreate_permissions(apps, schema_editor):
    AuthGroup = apps.get_model('groupmanagement', 'AuthGroup')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    ct = ContentType.objects.get_for_model(AuthGroup)
    Permission.objects.create(content_type=ct, name='Can add auth group', codename='add_authgroup')
    Permission.objects.create(content_type=ct, name='Can delete auth group', codename='delete_authgroup')
    Permission.objects.create(content_type=ct, name='Can change auth group', codename='change_authgroup')


class Migration(migrations.Migration):

    dependencies = [
        ('groupmanagement', '0007_on_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authgroup',
            options={'default_permissions': (), 'permissions': (('request_groups', 'Can request non-public groups'),)},
        ),
        migrations.RunPython(delete_permissions, recreate_permissions)
    ]
