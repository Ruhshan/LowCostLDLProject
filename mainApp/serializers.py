from rest_framework import serializers
from .models import QC

class QCSerializer(serializers.ModelSerializer):

    class Meta:
        model = QC
        fields = ['test_name', 'lower_range', 'upper_range']