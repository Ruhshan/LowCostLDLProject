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

    def get_data_points_count(self):
        ct=0
        for up in self.userprofile_set.all():
            ct+=up.user.datapoint_set.count()
        return ct

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


class DataPoint(models.Model):
    sex_choices = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    category_choices = (
        ('regular', 'REGULAR'),
        ('qc', 'QC'),
    )

    patient_id = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=2, choices=sex_choices)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    data_category = models.CharField(max_length=10,choices=category_choices,null=True, blank=True, )
    total_cholesterol = models.IntegerField()
    high_density_lipid = models.IntegerField()
    low_density_lipid = models.IntegerField()
    tri_glycerides = models.IntegerField()
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, blank=True)
    district = models.CharField(max_length=50,null=True, blank=True)

    def get_absolute_url(self):
        return reverse('mainapp:data-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.data_category)[:2]+'_'+str(self.id)


class QC(models.Model):
    test_name = models.CharField(max_length=50)
    qc_name = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    level_1_lower_range = models.IntegerField()
    level_2_lower_range = models.IntegerField()
    level_3_lower_range = models.IntegerField()

    level_1_upper_range = models.IntegerField()
    level_2_upper_range = models.IntegerField()
    level_3_upper_range = models.IntegerField()

    added_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, blank=True)
    district = models.CharField(max_length=50,null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)


    def __str__(self):
        return self.test_name
    def get_absolute_url(self):
        return reverse('mainapp:qc-detail', kwargs={'pk': self.pk})

class QCData(models.Model):
    level_choices=(('1','1'),
                    ('2','2'),
                    ('3','3'))
    test_name = models.ForeignKey(QC, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=level_choices)
    value = models.IntegerField()
    remarks = models.CharField(max_length=50)
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, blank=True)
    district = models.CharField(max_length=50,null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.test_name)+str(self.id)

    def get_absolute_url(self):
        return reverse('mainapp:data-qc-detail', kwargs={'pk': self.pk})



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
