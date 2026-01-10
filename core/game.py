from .team import Team
from .player import Player
import random

class Game:
    def __init__(self, player: Player, cpu_team: Team) -> None:
        self.player = player
        self.p_team = self.player.team
        self.cpu_team = cpu_team

    def Update(self) -> None:
        condition = self.Play()
        if condition == True:
            self.p_team.wins += 1
            self.player.wins += 1
        elif condition == False:
            self.p_team.losses += 1
            self.player.losses += 1
        else:
            self.p_team.ties += 1
            self.player.ties += 1

        if self.p_team.ties == 0:
            print(f'{self.p_team.wins}-{self.p_team.losses}')
        else:
            print(f'{self.p_team.wins}-{self.p_team.losses}-{self.p_team.ties}')
    
    def Play(self, post_season: bool = False) -> bool:
        # Generate random score between 0 and 100 for each team
        p_score = 7 * random.randint(0, 5) + 3 * random.randint(0, 5) + 3 * random.randint(0, self.player.rating)
        cpu_score = 7 * random.randint(0, 5) + 3 * random.randint(0, 5)

        # Determine winner
        if p_score > cpu_score:
            print(f'{self.p_team.name} won {p_score} to {cpu_score}!')
            return True
        elif p_score < cpu_score:
            print(f'{self.p_team.name} lost {p_score} to {cpu_score}!')
            return False
        else:
            if post_season == True:
                print(f'{self.p_team.name} won overtime {p_score + 6} to {cpu_score}!')
                return True
            else:
                print(f'{self.p_team.name} tied {p_score} to {cpu_score}!')
            return None