# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.


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

class UsersView(generic.ListView):
    template_name = 'mainApp/users.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all()

class UsersDetail(generic.DetailView):
    model = User
    template_name = 'mainApp/user_detail.html'

class UserAddView(View):
    def get(self, request):
        user_form = UserCreateForm()
        return render(request, 'mainApp/user_form.html',{'form':user_form})
    def post(self, request):
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.userprofile.lab = user_form.cleaned_data.get('lab')
            user.userprofile.designation = user_form.cleaned_data.get('designation')
            print user_form.cleaned_data.get('role')
            if str(user_form.cleaned_data.get('role')) == 'admin':
                admin_group = Group.objects.get(name='admin')
                user.groups.add(admin_group)

            if str(user_form.cleaned_data.get('role')) == 'user':
                user_group = Group.objects.get(name='user')
                user.groups.add(user_group)
            user.save()
            return HttpResponseRedirect(reverse('mainapp:user-detail', kwargs={'pk': user.pk}))

        return render(request, 'mainApp/user_form.html', {'form': user_form})


class UserUpdateView(View):
    def get(self, request, pk):
        user=User.objects.get(pk=pk)
        user_form = UserUpdateForm(instance=user)
        profile_form = PofileUpdateForm(instance=user.userprofile)
        role = user.groups.all()[0]
        return render(request, 'mainApp/user_form.html',{'form':user_form,'extra_form':profile_form,'role':role})

    def post(self, request, pk ):
        user = User.objects.get(pk=pk)
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = PofileUpdateForm(request.POST, instance=user.userprofile)
        role = user.groups.all()[0]
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            newrole = profile_form.cleaned_data.get('role')
            oldrole = str(user.groups.all()[0])
            if newrole!=None:
                if str(newrole) != str(oldrole):
                    new_role = Group.objects.get(name=newrole)
                    user.groups.clear()
                    user.groups.add(new_role)
                    print newrole, oldrole
            profile_form.save()
            return HttpResponseRedirect(reverse('mainapp:user-detail', kwargs={'pk': user.pk}))

        return render(request, 'mainApp/user_form.html', {'form': user_form,'role':role})




