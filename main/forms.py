from django import forms
from django.forms import ModelForm
from .models import Product

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

#class OptionsForm(forms.ModelForm):
#    class Meta:
#        model = OptionalExtras
#        fields = ['name', 'price']
