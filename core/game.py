import random
import pandas as pd
from .team import Team
from .player import Player

class Game:
    def __init__(self, player: Player, cpu_team: Team) -> None:
        self.player = player
        self.p_team = self.player.team
        self.cpu_team = cpu_team
    
    def Play(self) -> None:
        # Generate random score between 0 and 100 for each team
        p_score = 7 * random.randint(0, 5) + 3 * random.randint(0, 5)
        cpu_score = 7 * random.randint(0, 5) + 3 * random.randint(0, 5)

        # Determine winner
        if p_score > cpu_score:
            print(f'{self.p_team.name} won {p_score} to {cpu_score}!')
            self.p_team.wins += 1
        elif p_score < cpu_score:
            print(f'{self.p_team.name} lost {p_score} to {cpu_score}!')
            self.p_team.losses += 1
        else:
            print(f'{self.p_team.name} tied {p_score} to {cpu_score}!')
            self.p_team.ties += 1
        
        if self.p_team.ties == 0:
            print(f'{self.p_team.wins}-{self.p_team.losses}')
        else:
            print(f'{self.p_team.wins}-{self.p_team.losses}-{self.p_team.ties}')