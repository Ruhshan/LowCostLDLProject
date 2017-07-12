from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from Districts import dist_choices
from django.db.models.fields import BLANK_CHOICE_DASH

class UserCreateForm(UserCreationForm):
    lab = forms.ModelChoiceField(Lab.objects.all())
    designation = forms.CharField(max_length=50)
    role = forms.ModelChoiceField(Group.objects.all())
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2', 'lab', 'designation', 'role')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class PofileUpdateForm(forms.ModelForm):
    role = forms.ModelChoiceField(Group.objects.all(), required=False)
    class Meta:
        model = UserProfile
        fields = ('lab', 'designation', 'role')


class SearchForm(forms.Form):
    any_term = forms.CharField(max_length=50, required=False)
    district = forms.CharField(max_length=50, required=False)
    lab = forms.CharField(max_length=50, required=False)
    user = forms.CharField(max_length=50, required=False)
    patient_name = forms.CharField(max_length=50, required=False)
    patient_age = forms.IntegerField(required=False)

    date_start = forms.CharField(max_length=50, required=False)
    date_end = forms.CharField(max_length=50, required=False)

    class Meta:
        fields =('any_term', 'district','lab','user','date_start','date_end')

