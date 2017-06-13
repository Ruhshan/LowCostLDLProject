# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from Districts import dist_choices
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
#Create your models here.
class Lab(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    thana = models.CharField(max_length=50, blank=True)
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    district = models.CharField(max_length=2, choices=dist_choices)

    class Meta:
        unique_together =('name', 'thana')

    def get_absolute_url(self):
        return reverse('mainapp:lab-detail', kwargs={'pk': self.pk})

    def __str__(self):
        if self.thana:
            return self.name+':'+self.thana
        else:
            return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    lab = models.ForeignKey(Lab, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('mainapp:user-detail', kwargs={'pk': self.pk})

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()