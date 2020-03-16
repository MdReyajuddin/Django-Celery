from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField()