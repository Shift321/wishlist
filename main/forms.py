from typing import Text
from django import forms
from django.forms.fields import CharField


class CreateNewList(forms.Form):
    name = forms.CharField(label="name", max_length=200,help_text="Put here name of your wishlist")
    check = forms.BooleanField(required=False)
