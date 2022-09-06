from django import forms
from django.contrib.auth.models import User
from .models import Room

# class Dataform(forms.Form):
#     name = forms.CharField(max_length=100)
#     topic = forms.CharField(max_length=200)
#     description = forms.Textarea()
#     theme = forms.CharField(max_length=100)
    # user = forms.ModelChoiceField(User)

class Dataform(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'topic', 'description', 'theme', 'user']