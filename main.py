from core.player import Player
from core.team import Team
from core.season import Season
from core.debug import debug
from core.typing import type_effect
import pandas as pd
import config

def main():
    # 1. Create player
    if debug:
        rating = int(input('[RATING (1-5)] '))
    else:
        rating = 0
    name = input('[NAME] ')
    year = int(input('[YEAR] '))
    player = Player(name=name, rating=rating)

    # 2. Draft player to team
    player_team = Team(config.teams)
    config.teams = config.teams[config.teams['Name'] != player_team.name]
    config.teams = config.teams.reset_index(drop=True)
    player.Draft(team=player_team, year_joined=year)

    # 3. Seasons loop
    while True:
        # Entire season
        Season(player=player, year=year).Start()
        year += 1
        
        # Retire option
        retire = input('\nRETIRE? [Y/N] ')
        if retire.lower() == 'y':
            break
        else:
            print(type_effect('You get ready for another season.'))

if __name__ == '__main__':
    main()