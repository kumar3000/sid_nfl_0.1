from .team import Team
from .player import Player
import random
import time

# Mini game that returns the # of touchdowns a player has thrown in the game
def Mini_Game(player: Player) -> int:
    p_tds = 0 # Worst case scenario

    # Game sim
    delay = random.randint(1, 5)
    print("Driving...")
    time.sleep(delay)
    t = time.time() # Start time
    input("PASS!")
    score = time.time() - t
    print(f"\nScore: {score:.2f}\n")
    
    # TD calculation
    if score < 0.2:
        p_tds = 3
    elif score < 0.35:
        p_tds = 2
    elif score < 0.5:
        p_tds = 1

    player.tds += p_tds
    player.season_tds += p_tds
    return p_tds

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
        # p_tds = random.randint(0, self.player.rating)
        p_tds = Mini_Game(self.player)
        cpu_tds = random.randint(0, p_tds)
        p_score = 7 * random.randint(0, cpu_tds) + 7 * p_tds + 3 * random.randint(0, 3)
        cpu_score = 7 * random.randint(0, 2) + 7 * cpu_tds + 3 * random.randint(0, 3)
        if p_score == cpu_score:
            p_score += random.randint(0, 1) * 3

        # Determine winner
        if p_score > cpu_score:
            print(f'{self.p_team.name} won {p_score} to {cpu_score}!')
            print(f'{self.player.name} scored {p_tds} TDs!')
            return True
        elif p_score < cpu_score:
            print(f'{self.p_team.name} lost {p_score} to {cpu_score}!')
            print(f'{self.player.name} scored {p_tds} TDs.')
            return False
        else:
            if post_season == True:
                print(f'{self.p_team.name} won overtime {p_score + 6} to {cpu_score}!')
                print(f'{self.player.name} scored {p_tds} TDs!')
                return True
            else:
                print(f'{self.p_team.name} tied {p_score} to {cpu_score}!')
                print(f'{self.player.name} scored {p_tds} TDs.')
            return None
