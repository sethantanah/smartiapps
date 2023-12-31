from django.forms import ModelForm
from django import forms

from .models import Files


class FileForm(ModelForm):
    class Meta:
        model = Files
        fields = ['file', 'title', 'description', 'file_type', 'file_url', 'price']

    description = forms.Textarea()
