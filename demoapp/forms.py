from django import forms
from django.forms import ModelForm
from .models import *

class PlaceAddForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'desc', 'image']
        widgets = {
            'name': forms.TextInput(),
            'desc': forms.Textarea(),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class UserAddForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'desc', 'profile']
        widgets = {
            'name': forms.TextInput(),
            'desc': forms.Textarea(),
            'profile': forms.FileInput(attrs={'accept': 'image/*'}),
        }