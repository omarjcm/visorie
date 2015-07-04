# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institutos_educativos',
            old_name='ie_geom',
            new_name='geom',
        ),
    ]
