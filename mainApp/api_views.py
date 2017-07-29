from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from .models import QC
from .serializers import QCSerializer


class QCRangeAPIView(RetrieveAPIView):
    queryset = QC.objects.all()
    serializer_class = QCSerializer


