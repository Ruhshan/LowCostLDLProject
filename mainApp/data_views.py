# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *
from .forms import *
from .my_tables import *
from django_tables2 import *
# Create your views here.

class DataAdd:
    model = DataPoint
    fields = ['patient_id', 'patient_name', 'age', 'gender', 'total_cholesterol', 'high_density_lipid',
              'low_density_lipid',
              'tri_glycerides']

class DataAddReView(DataAdd, generic.CreateView):
    def form_valid(self, form):
        data = form.save()
        data.added_by = self.request.user
        data.data_category = 'regular'
        data.save()
        return HttpResponseRedirect(reverse('mainapp:data-detail', kwargs={'pk': data.pk}))

class DataAddQcView(DataAdd, generic.CreateView):
    def form_valid(self, form):
        data = form.save()
        data.added_by = self.request.user
        data.data_category = 'qc'
        data.save()
        return HttpResponseRedirect(reverse('mainapp:data-detail', kwargs={'pk': data.pk}))


class DataDetails(generic.DetailView):
    model = DataPoint
    template_name = 'mainApp/datapoint_detail.html'

class HomeView(View):
    template_name = 'mainApp/view_data.html'
    def get(self, request):
        datapoints = DataPoint.objects.all()
        return render(request,self.template_name, {'datapoints':datapoints})
