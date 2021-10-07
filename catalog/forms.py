import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class MarkVisitForm(forms.Form):

    CHOICES = (('a', 'Awaiting'),
        ('c', 'Completed'),
        ('n', 'Not completed'),)
    new_mark = forms.ChoiceField(choices=CHOICES)

    def clean_new_mark(self):
        data = self.cleaned_data['new_mark']

                
        return data


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean_first_name(self):
        data = self.cleaned_data['first_name']

        
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']

        return data

    def clean_email(self):
        data = self.cleaned_data['email']

        
        return data