import core.player as player
import core.team as team
import pandas as pd

player = player.Player('John Doe', team.Team(pd.read_csv(r'docs/club_data.csv')))
print(player.name + ' is on the ' + player.team.name + ' ' + player.team.conference + ' ' + player.team.division + ' division.')   