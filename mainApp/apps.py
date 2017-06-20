# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson

class MainappConfig(AppConfig):
    name = 'mainApp'
    def ready(self):
        DataPoint = self.get_model('DataPoint')
        watson.register(DataPoint,fields=('patient_name','age','added_by','date','gender','district','lab','total_cholesterol','high_density_lipid','low_density_lipid','tri_glycerides'))
