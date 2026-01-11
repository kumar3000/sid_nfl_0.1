from core.player import Player
from core.team import Team
from core.season import Season
from core.debug import debug
import pandas as pd
import config

def main():
    # Create player
    if debug:
        rating = int(input('[RATING (1-5)] '))
    else:
        rating = 0
    name = input('[NAME] ')
    year = int(input('[YEAR] '))
    player = Player(name=name, rating=rating)
    print(f'Welcome {player.name}!')

    # Draft player to team
    player_team = Team(config.teams)
    config.teams = config.teams[config.teams['Name'] != player_team.name]
    config.teams = config.teams.reset_index(drop=True)
    player.Draft(team=player_team, year_joined=year)

    # Seasons loop
    Season(player=player, year=year).Start()

if __name__ == '__main__':
    main()