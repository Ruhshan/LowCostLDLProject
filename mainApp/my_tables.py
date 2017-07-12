import django_tables2 as tables
from .models import *

class DataPointTable(tables.Table):
    class Meta:
        model = DataPoint
        attrs = {'id': 'grid'}
