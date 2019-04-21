# Web App
For now this is just following the [Django Tutorial](https://docs.djangoproject.com/en/2.2/intro/).
Let's see where it goes from there.   :-)


# Kicker App

The Kicker (aka Foosball) app is an app to track game results.
It can be found in the [kicker](mysite/kicker) folder.


## Dependencies

Install dependencies exported from [Anaconda](https://www.anaconda.com) [environment file](environment.yml).


## Features

Currently a list of players can be maintained.
New games can be added, setting 2 home and 2 guest players, as well as the game result.
Very basic statistics about players are being generated right now: Number of games played, games won and the win ratio.


### Future

 - More player statistics
   - Number of games played with individual other players
   - Number of games played against individual other players
   - Ranking of all players according to different metrics
     - Win Ratio
     - Games Played
     - Games Won
 - Allow player avatars, nicknames
 - Team statistics
   - Introduction of team names?
   - Team Statistics?
      - Ranking of best teams
 - Heavily improve UI
 - Offer an API version to allow interaction with external (e.g. Raspberry Pi) sources
