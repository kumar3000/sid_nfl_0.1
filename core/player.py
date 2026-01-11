from .team import Team
from .typing import type_input, type_effect
import random

class Player:
    def __init__(self, name: str, rating: int = 0) -> None:
        self.name = name
        self.rating = rating
        self.seasons = 0

        # Player stats
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.tds = 0

        # Seasonal stats
        self.season_tds = 0

        # Post season stats
        self.super_bowls = []
        self.mvps = []
        self.post_wins = 0
        self.post_losses = 0
        self.post_ties = 0

    def Draft(self, team: Team) -> None:
        # Assign team
        self.team = team
        print(type_effect('The ' + self.team.name + ' select ' + self.name + '!'))

        # Generate rating between 5* and 1* QB
        if self.rating == 0: # If no rating is provided (rating not provided in constructor), generate a random one
            self.rating = random.randint(1, 5)
        print(type_effect(f'{self.name} is a {int(self.rating)} Star player!'))

    def DisplayStats(self) -> None:
        # Career record
        if self.ties == 0:
            print(type_effect(f'[CAREER RECORD] {self.wins}-{self.losses}'), end=' ')
        else:
            print(type_effect(f'[CAREER RECORD] {self.wins}-{self.losses}-{self.ties}'), end=' ')
        print(type_effect(f'[POST SEASON RECORD] {self.post_wins}-{self.post_losses}'))

        # Seasonal and career TDs
        print(type_effect(f'[SEASON TDs] {self.season_tds}'), end=' ')
        print(type_effect(f'[CAREER TDs] {self.tds}'), end=' ')

        # MVP awards
        if len(self.mvps) > 0:
            print(type_effect(f'[MVPs]'), end=' ')
            for mvp in self.mvps:
                print(type_effect(f'({mvp} {self.team.abbreviation})'), end=' ')

        # Super bowls
        if len(self.super_bowls) > 0:
            print(type_effect(f'\n[SUPER BOWLS]'), end=' ')
            for super_bowl in self.super_bowls:
                print(type_effect(f'{super_bowl}'), end=' ')