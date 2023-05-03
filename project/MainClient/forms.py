from .models import *
from django import forms
from django.forms import formset_factory

class AddToCartForm(forms.Form):
    slug = forms.CharField()
    quantity = forms.IntegerField(min_value=1)


AddToCartFormSet = formset_factory(AddToCartForm, extra=1)
