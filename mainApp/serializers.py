from rest_framework import serializers
from .models import QC

class QCSerializer(serializers.ModelSerializer):

    class Meta:
        model = QC
        fields = ['test_name', 'level_1_lower_range', 'level_1_upper_range',
                  'level_2_lower_range', 'level_2_upper_range',
                  'level_3_lower_range', 'level_3_upper_range'
                  ]