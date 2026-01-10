from .team import Team
from .typing import type_input, type_effect
import random

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rating = 0
        self.seasons = 0

        # Player stats
        self.wins = 0
        self.losses = 0
        self.ties = 0

        # Post season stats
        self.super_bowls = []
        self.post_wins = 0
        self.post_losses = 0
        self.post_ties = 0

    def Draft(self, team: Team) -> None:
        # Assign team
        self.team = team
        print(type_effect('The ' + self.team.name + ' select ' + self.name + '!'))

        # Generate rating between 5* and 1* QB
        self.rating = random.randint(1, 5)
        print(type_effect(f'{self.name} is a {int(self.rating)} Star player!'))

    def DisplayStats(self) -> None:
        print(type_effect(f'[CAREER RECORD {self.wins}-{self.losses}-{self.ties}]'))
        print(type_effect(f'[POST SEASON RECORD {self.post_wins}-{self.post_losses}]'))
        print(type_effect(f'[SUPER BOWLS]'), end=' ')
        for super_bowl in self.super_bowls:
            print(type_effect(f'{super_bowl}]'), end=' ')