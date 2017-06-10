# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.views import generic
from django.http import HttpResponse
from .models import *
# Create your views here.

class HomeView(View):
    template_name = 'mainApp/base.html'
    def get(self, request):
        return render(request,self.template_name)

class LabsView(generic.ListView):
    template_name = 'mainApp/labs.html'
    context_object_name = 'all_labs'

    def get_queryset(self):
        return Lab.objects.all()

class LabsDetail(generic.DetailView):
    model = Lab
    template_name = 'mainApp/lab_detail.html'

class LabAddView(generic.CreateView):
    model = Lab
    fields = ['name','address','thana','district']

class LabUpdate(generic.UpdateView):
    model = Lab
    fields = ['name', 'address', 'thana', 'district']
