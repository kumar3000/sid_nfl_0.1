from core.player import Player
from core.team import Team
from core.season import Season
import pandas as pd
import config

def main():
    # Create player
    name = input('NAME: ')
    year = int(input('YEAR: '))
    player = Player(name=name)
    print(f'Welcome {player.name}!')

    # Draft player to team
    player_team = Team(config.teams)
    config.teams = config.teams[config.teams['Name'] != player_team.name]
    config.teams = config.teams.reset_index(drop=True)
    player.Draft(team=player_team)

    # Seasons loop
    Season(player=player, year=year).Start()

if __name__ == '__main__':
    main()