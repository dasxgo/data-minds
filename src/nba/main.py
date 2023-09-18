import pandas as pd
import numpy as np
import load
from utils import top_scorers

df = load.data1
print('-'*120)

def main():
    print(df.head())
    print('-'*120)
    max_height_player = df[['player_name', 'player_height', 'country']].max()
    print(f'Player with highest height:{max_height_player}')
    print('-'*120)
    min_height_player = df[['player_name', 'player_height', 'country']].min()
    print(f'Shorter player:{min_height_player}')
    print('-'*120)
    max_weight_player = df[['player_name', 'player_weight', 'country']].max()
    print(f'Player with highest weight:{max_weight_player}')
    print('-'*120)
    min_weight_player = df[['player_name', 'player_weight', 'country']].min()
    print(f'Lightest player:{min_weight_player}')
    print('-'*120)
    print(top_scorers)
    
if __name__ == '__main__':
    main()




