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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class IsAdmin(UserPassesTestMixin):
    def test_func(self):
        try:
            return 'admin' == str(self.request.user.groups.all()[0])
        except:
            return False

class LoginRequired(LoginRequiredMixin):
    login_url = '/login/'


class LabsView(IsAdmin, LoginRequired, generic.ListView):
    template_name = 'mainApp/labs.html'
    context_object_name = 'all_labs'
    search_form = SearchForm
    def get_queryset(self):
        return Lab.objects.all()

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()

        if 'search_form' not in context:
            context['search_form'] = self.search_form()
            context['district_list'] = district_list
            context['labs'] = labs
            context['users'] = users
        return context



class LabsDetail(IsAdmin, LoginRequired,generic.DetailView):
    model = Lab
    template_name = 'mainApp/lab_detail.html'
    search_form = SearchForm

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()

        if 'search_form' not in context:
            context['search_form'] = self.search_form()
            context['district_list'] = district_list
            context['labs'] = labs
            context['users'] = users
        return context

class LabAddView(IsAdmin, LoginRequired,generic.CreateView):
    model = Lab
    fields = ['name','address','thana','district']
    search_form = SearchForm

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()

        if 'search_form' not in context:
            context['search_form'] = self.search_form()
            context['district_list'] = district_list
            context['labs'] = labs
            context['users'] = users
        return context



class LabUpdate(IsAdmin, LoginRequired, generic.UpdateView):
    model = Lab
    fields = ['name', 'address', 'thana', 'district']
    search_form = SearchForm

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()

        if 'search_form' not in context:
            context['search_form'] = self.search_form()
            context['district_list'] = district_list
            context['labs'] = labs
            context['users'] = users
        return context


class UsersView( LoginRequired,IsAdmin, generic.ListView):
    template_name = 'mainApp/users.html'
    context_object_name = 'all_users'
    search_form = SearchForm

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()

        if 'search_form' not in context:
            context['search_form'] = self.search_form()
            context['district_list'] = district_list
            context['labs'] = labs
            context['users'] = users
        return context

    def get_queryset(self):
        return User.objects.all()

class UsersDetail(IsAdmin,LoginRequired,generic.DetailView):
    model = User
    template_name = 'mainApp/user_detail.html'
    search_form = SearchForm

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()

        if 'search_form' not in context:
            context['search_form'] = self.search_form()
            context['district_list'] = district_list
            context['labs'] = labs
            context['users'] = users
        return context


class UserAddView(IsAdmin,LoginRequired, View):

    def get(self, request):
        user_form = UserCreateForm()
        search_form = SearchForm()
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()
        return render(request, 'mainApp/user_form.html',{'form':user_form, 'search_form':search_form,'district_list':district_list,
                                                  'labs':labs,'users':users})
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



class UserUpdateView(IsAdmin,LoginRequired,View):
    def get(self, request, pk):
        user=User.objects.get(pk=pk)
        user_form = UserUpdateForm(instance=user)
        profile_form = PofileUpdateForm(instance=user.userprofile)
        role = user.groups.all()[0]
        search_form = SearchForm()
        district_list = list(dist_choices)
        labs = Lab.objects.all().values('name')
        users = User.objects.all()
        return render(request, 'mainApp/user_form.html',{'form':user_form,'extra_form':profile_form,'role':role,'search_form':search_form,'district_list':district_list,
                                                  'labs':labs,'users':users})

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




