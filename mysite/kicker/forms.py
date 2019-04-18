from django import forms

from .models import Game, Player

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name',)
    
    # way to validate a single field is to override the method
    # clean_<fieldname>() for the field you want to check


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('home_player_1',
                  'home_player_2',
                  'guest_player_1',
                  'guest_player_2',)
    
    # way to validate a single field is to override the method
    # clean_<fieldname>() for the field you want to check