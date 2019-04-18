import datetime

from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateTimeField('date')

    # The involved players
    # TODO: Handle single player games
    home_player_1 = models.ForeignKey(Player,
                                      on_delete=models.PROTECT,
                                      related_name='home_player_1')
    home_player_2 = models.ForeignKey(Player,
                                      on_delete=models.PROTECT,
                                      related_name='home_player_2')
    guest_player_1 = models.ForeignKey(Player,
                                       on_delete=models.PROTECT,
                                       related_name='guest_player_1')
    guest_player_2 = models.ForeignKey(Player,
                                       on_delete=models.PROTECT,
                                       related_name='guest_player_2')


    # TODO: Tuple in the form of (home_goals, guest_goals)
    #result = (models.PositiveSmallIntegerField, models.PositiveSmallIntegerField)

    # Future TODO options here:
    # Save history of which player shot which goal
    # Add CharField for any comments on the game

    def __str__(self):
        return self.date