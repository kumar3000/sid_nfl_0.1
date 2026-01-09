from dataclasses import dataclass
from .team import Team

@dataclass
class Player:
    def __init__(self, name: str, team: Team):
        self.name = name
        self.team = team