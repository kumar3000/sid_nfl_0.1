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
        post_str = ''
        awards_str = ''
        
        # Career loop
        self.player.seasons += 1
        self.player.team.wins = 0
        self.player.team.losses = 0
        self.player.team.ties = 0
        self.player.season_tds = 0

        # Season header
        print(type_effect(f'\n--| {self.year} NFL SEASON |--| SEASON #{self.player.seasons} |--'))
        bye = random.randint(5, 14)
        print(type_effect(f'\n[WEEK {bye + 1} BYE]\n'))
        print(type_input('BEGIN SEASON? [ENTER]'))

        # Regular season
        if self.year >= 2021:
            games = 18
        else:
            games = 17
        
        for week in range(games):
            if week == bye:
                print(f'[WEEK {week + 1}] BYE WEEK')
            else:
                cpu_team = Team(config.teams)
                print(f'[WEEK {week + 1}] {self.player.team.name} vs {cpu_team.name}')
                Game(player=self.player, cpu_team=cpu_team).Update()
            input('')
            
            # Awards
        if self.player.team.wins >= 13:
            self.player.mvps.append(f'({self.year} {self.player.team.abbreviation})')
            awards_str = f' [MVP]'

        # Post season
        post_bye = False
        if self.player.team.losses <= 7: # If you made the playoffs...
            print(type_effect(f'--| {self.year} POST SEASON |--| SEASON #{self.player.seasons} |--\n'))
            if self.player.team.losses <= 3:
                post_bye = True
                
            # Post season games loop
            games = ['WILD CARD', 'DIVISIONAL ROUND', f'{self.player.team.conference} CHAMPIONSHIP', 'SUPER BOWL']
            if post_bye == True:
                print(type_effect(f'[FIRST ROUND BYE]\n'))
                games.pop(0)
            for week in games:
                post_str = f' [{week}]'
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
                    if week == 'SUPER BOWL':
                        post_str = f' [{cpu_team.abbreviation} v {self.player.team.abbreviation}]'
                    break
                elif post_won == True:
                    self.player.post_wins += 1
                    self.player.wins += 1
                if week == 'SUPER BOWL':
                    self.player.super_bowls.append(f'({self.year} {self.player.team.abbreviation} v {cpu_team.abbreviation})')
                    post_str = f' [{self.player.team.abbreviation} v {cpu_team.abbreviation}]'

        else: # If you missed the playoffs... (you can't win a playoff game)
            print(type_effect('You missed the playoffs this season.'))

        # End of season stats
        self.player.DisplayStats()

        # Append season info to career_seasons
        if self.player.team.ties > 0:
            season_info = f'[{self.year} {self.player.team.abbreviation}] {self.player.team.wins}-{self.player.team.losses}-{self.player.team.ties}'
        else:
            season_info = f'[{self.year} {self.player.team.abbreviation}] {self.player.team.wins}-{self.player.team.losses}'
        season_info += post_str
        season_info += awards_str
        self.player.career_seasons.append(season_info)
        self.player.DisplaySeasons()

        # Option to switch teams
        switch = input('\nSWITCH TEAMS? [Y/N] ')
        if switch.lower() == 'y':
            config.teams.loc[len(config.teams)] = self.player.team.team_data
            self.player.SwitchTeam(Team(config.teams), year_joined=self.year)
        else:
            print(type_effect(f'You decided to stay with the {self.player.team.name}.'))