import random
from .team import Team

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rating = 0

    def Draft(self, team: Team) -> None:
        # Assign team
        self.team = team
        print('The ' + self.team.name + ' select ' + self.name + '!')

        # Generate rating between 5* and 1* QB
        self.rating = 5*random.randint(1, 5)
        print(f'{self.name} is a {int(self.rating / 5)} Star player!')