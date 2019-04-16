from django import forms

from .models import Player

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name',)
    
    # way to validate a single field is to override the method
    # clean_<fieldname>() for the field you want to check