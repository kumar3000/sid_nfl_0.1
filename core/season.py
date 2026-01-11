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
        print(type_input('\nSTART? [ENTER]'))

        # Career loop
        while self.player.seasons < 20:
            self.player.seasons += 1
            self.player.team.wins = 0
            self.player.team.losses = 0
            self.player.team.ties = 0
            self.player.season_tds = 0

            # Season header
            print(type_effect(f'--| {self.year} NFL SEASON |--| SEASON #{self.player.seasons} |--'))
            bye = random.randint(5, 14)
            print(type_effect(f'\n[WEEK {bye + 1} BYE]\n'))
            print(type_input('BEGIN SEASON? [ENTER]'))

            # Regular season
            for week in range(18):
                if week == bye:
                    print(f'[WEEK {week + 1}] BYE WEEK')
                else:
                    cpu_team = Team(config.teams)
                    print(f'[WEEK {week + 1}] {self.player.team.name} vs {cpu_team.name}')
                    Game(player=self.player, cpu_team=cpu_team).Update()
                input('')
            
            # Awards
            if self.player.season_tds >= 45:
                self.player.mvps.append(f'({self.year} {self.player.team.abbreviation})')

            # Post season
            post_bye = False
            if self.player.team.losses <= 7: # If you made the playoffs...
                print(type_effect(f'--| {self.year} POST SEASON |--| SEASON #{self.player.seasons} |--\n'))
                if self.player.team.losses <= 3:
                    post_bye = True
                
                # Post season games loop
                games = ['WILD CARD', 'DIVISIONAL ROUND', 'CONFERENCE CHAMPIONSHIP', 'SUPER BOWL']
                if post_bye == True:
                    print(type_effect(f'[FIRST ROUND BYE]\n'))
                    games.pop(0)
                for week in games:
                    if week != 'SUPER BOWL':
                        cpu_team = Team(config.teams[config.teams['Conference'] == self.player.team.conference])
                    else:
                        cpu_team = Team(config.teams[config.teams['Conference'] != self.player.team.conference])
                    print(type_effect(f'[{week}] {self.player.team.name} vs {cpu_team.name}'))
                    post_won = Game(player=self.player, cpu_team=cpu_team).Play(post_season=True)
                    input('')
                    if post_won == False:
                        self.player.post_losses += 1
                        self.player.losses += 1
                        break
                    elif post_won == True:
                        self.player.post_wins += 1
                        self.player.wins += 1
                    if week == 'SUPER BOWL':
                        self.player.super_bowls.append(f'({self.year} {self.player.team.abbreviation} v {cpu_team.abbreviation})')

            else: # If you missed the playoffs... (you can't win a playoff game)
                print(type_effect('You missed the playoffs this season.'))

                # Option to switch teams
                switch = input('Switch teams? [Y/N] ')
                if switch.lower() == 'y':
                    config.teams.loc[len(config.teams)] = self.player.team.team_data
                    self.player.SwitchTeam(Team(config.teams), year_joined=self.year)
                else:
                    print(type_effect('You will remain with your current team.\n'))

            self.player.DisplayStats()

            # Continue loop
            print(type_input('\n\nNEXT SEASON? [ENTER]'))
            self.year += 1