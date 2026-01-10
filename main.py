from core.player import Player
from core.team import Team
from core.game import Game
import pandas as pd

def main():
    # Create player
    name = input('Enter your name: ')
    player = Player(name=name)
    print(f'Welcome {player.name}!')

    # Draft player to team
    player.Draft(team=Team(pd.read_csv(r'docs/club_data.csv')))

    # Seasons loop
    run = True
    while run == True:
        # Test game
        Game(player=player, cpu_team=Team(pd.read_csv(r'docs/club_data.csv'))).Play()

        # Continue loop
        cont = input('[ENTER to CONTINUE]\n')
        if cont.lower() == 'n':
            run = False

if __name__ == '__main__':
    main()