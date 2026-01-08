import pandas as pd
import numpy as np

file_path = r'..\docs\club_data.csv'
team_data = pd.read_csv(file_path)

def start():
    player_name = input("Enter your name: ")
    print(f"Welcome {player_name} to the NFL 0.1")
    random_team = team_data.sample(1)
    print(f"You have been drafted by the {random_team['Name'].values[0]}")

start()