from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserCreateForm(UserCreationForm):
    lab = forms.ModelChoiceField(Lab.objects.all())
    designation = forms.CharField(max_length=50)
    role = forms.ModelChoiceField(Group.objects.all())
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email', 'password1', 'password2', 'lab', 'designation', 'role')