import datetime

from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')

    def __str__(self):
        return f'{self.name}'


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
    # Write unit test for the winner team etc. methods

    def home_won(self):
        return (self.home_goals > self.guest_goals)
    
    def guest_won(self):
        return (self.guest_goals > self.home_goals)

    def get_home_team_players(self):
        return [self.home_player_1, self.home_player_2]
    
    def get_guest_team_players(self):
        return [self.guest_player_1, self.guest_player_2]

    def is_in_home_team(self, player):
        if player in self.get_home_team_players():
            return True
        else:
            return False
    
    def is_in_guest_team(self, player):
        if player in self.get_guest_team_players():
            return True
        else:
            return False
    
    def get_winner_team(self):
        if self.home_won():
            return self.get_home_team_players()
        elif self.guest_won():
            return self.get_guest_team_players()
    
    def is_winner_team_member(self, player):
        if player in self.get_winner_team():
            return True
        else:
            return False

    def __str__(self):
        return f'{self.id}: {self.home_player_1}/{self.home_player_2} {self.home_goals} - {self.guest_goals} {self.guest_player_1}/{self.guest_player_2} {self.date.strftime("%Y-%m-%d %H:%M")}'
