from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from Districts import dist_choices
from django.db.models.fields import BLANK_CHOICE_DASH
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions

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


class QCForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                'QC Information',
                Div(Field('test_name')),
                Div(Field('qc_name')),
                Div(Field('lot')),
                Div(
                    Div(Field('level_1_lower_range'), css_class='col-sm-6'),
                    Div(Field('level_1_upper_range'), css_class='col-sm-6'),
                    css_class="row"),
                Div(
                    Div(Field('level_2_lower_range'), css_class='col-sm-6'),
                    Div(Field('level_2_upper_range'), css_class='col-sm-6'),
                    css_class="row"),
                Div(
                    Div(Field('level_3_lower_range'), css_class='col-sm-6'),
                    Div(Field('level_3_upper_range'), css_class='col-sm-6'),
                    css_class="row"),
            ),
            FormActions(
                Submit('submit', 'Save', css_class='btn btn-primary')
            )
        )

        super(QCForm, self).__init__(*args, **kwargs)
    class Meta:
        model = QC
        exclude = ['district', 'added_by','lab']
