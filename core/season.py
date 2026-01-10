from .player import Player
from .team import Team
from .game import Game
from .typing import type_input, type_effect
import pandas as pd
import random
import config

class Season:
    def __init__(self, player: Player, year: int) -> None:
        self.player = player
        self.year = year

    def Start(self) -> None:
        print(type_input('START? [ENTER]'))

        # Career loop
        while self.player.seasons < 20:
            self.player.seasons += 1
            self.player.team.wins = 0
            self.player.team.losses = 0
            self.player.team.ties = 0

            # Season header
            print(type_effect(f'--| {self.year} NFL SEASON |--'))
            print(type_effect(f'[REGULAR SEASON {self.player.seasons}]'))
            bye = random.randint(5, 14)
            print(type_effect(f'[WEEK {bye + 1} BYE]\n'))

            # Regular season
            for week in range(18):
                if week == bye:
                    print(f'[WEEK {week + 1}] BYE WEEK')
                else:
                    cpu_team = Team(config.teams)
                    print(f'[WEEK {week + 1}] {self.player.team.name} vs {cpu_team.name}')
                    Game(player=self.player, cpu_team=cpu_team).Update()
                input(' ')

            # Post season
            post_bye = False
            if self.player.team.losses <= 7: # If you made the playoffs...
                print(type_effect('[POST SEASON]\n'))
                if self.player.team.losses <= 3:
                    post_bye = True
                
                # Post season games loop
                games = ['WILD CARD', 'DIVISIONAL', 'CONFERENCE CHAMPIONSHIP', 'SUPER BOWL']
                if post_bye == True:
                    print(type_effect(f'[FIRST ROUND BYE]\n'))
                    games.pop(0)
                for week in games:
                    cpu_team = Team(config.teams)
                    print(type_effect(f'[{week}] {self.player.team.name} vs {cpu_team.name}'))
                    post_won = Game(player=self.player, cpu_team=cpu_team).Play(post_season=True)
                    input(' ')
                    if post_won == False:
                        self.player.post_losses += 1
                        break
                    elif post_won == True:
                        self.player.post_wins += 1
                        
                    if week == 'SUPER BOWL':
                        self.player.super_bowls.append(self.year)

            else: # If you missed the playoffs... (you can't win a playoff game)
                print(type_effect('You missed the playoffs this season.'))
            
            self.player.DisplayStats()

            # Continue loop
            print(type_input('\nNEXT SEASON? [ENTER]'))
            self.year += 1