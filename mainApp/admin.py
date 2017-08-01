# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
admin.site.register(Lab)
admin.site.register(UserProfile)
admin.site.register(DataPoint)
admin.site.register(QCData)
admin.site.register(QC)
