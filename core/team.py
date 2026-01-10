from dataclasses import dataclass
import pandas as pd
import random

@dataclass
class Team:
    def __init__(self, DataFrame: pd.DataFrame) -> None:
        self.team_data = DataFrame.iloc[random.randint(0, len(DataFrame) - 1)] # random team each time team(DataFrame) is called
        self.name = self.team_data['Name']
        self.id = self.team_data['ID']
        self.abbreviation = self.team_data['Abbreviation']
        self.conference = self.team_data['Conference']
        self.division = self.team_data['Division']

        # Team stats
        self.wins = 0
        self.losses = 0
        self.ties = 0