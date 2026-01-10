from core import player, team
import pandas as pd

# Create player
name = input('Enter your name: ')
player = player.Player(name, team.Team(pd.read_csv(r'docs/club_data.csv')))
print(f'Welcome {player.name}!')

# Draft player to team
player.Draft(team.Team(pd.read_csv(r'docs/club_data.csv')))
print('The ' + player.team.name + ' select ' + player.name + '!')