import datetime

from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')

    def __str__(self):
        return f'{self.id}: {self.name} {self.join_date.strftime("%Y-%m-%d")}'

class Game(models.Model):
    # Date and time of the game
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

    # Final result of the game
    home_goals = models.PositiveSmallIntegerField(default=0)
    guest_goals =  models.PositiveSmallIntegerField(default=0)

    # TODO:
    # Save history of which player shot which goal
    # Add CharField for any comments on the game

    def __str__(self):
        return f'{self.id}: {self.home_player_1}/{self.home_player_2} {self.home_goals} - {self.guest_goals} {self.guest_player_1}/{self.guest_player_2} {self.date.strftime("%Y-%m-%d %H:%M")}'
