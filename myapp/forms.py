from django import forms 
from django.forms import ModelForm 

from myapp.models import Flowers 


class MyForm(ModelForm):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={
        'class':'py-2 px-2 rounded-md w-64'
    }))

    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        'class':'py-x px-2 rounded-md mt-2 w-64'
    }))

    # category = forms.CharField(label="Category", widget=forms.SelectMultiple(attrs={
    #     'class':'py-x px-2 rounded-md mt-2'
    # }))

    # tags = forms.CharField(label="Tag", widget=forms.SelectMultiple(attrs={
    #     'class':'py-x px-2 rounded-md mt-2'
    # }))
    class Meta:
        model = Flowers
        exclude = ('slug','category', 'tags')