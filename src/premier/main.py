import pandas as pd
import numpy as np
import utils 
import load

df = load.df_stats

def main():
    print(df.head())
    print('-'*120)
    print(df.shape)
    print('-'*120)
    print(df[0:7])
    print('-'*120)
    print(df.describe())

    print('='*120)

    # Finding the teams with total wins, losses and draws per total matches
    # Creating a new column draws
    
    df['draws'] = 38 - df['wins'] - df['losses']
    
    # Changing the column location
    pop_column = df.pop('draws')
    df.insert(3, 'draws', pop_column)
    
    # Creating a new column total_matches
    
    df['total_matches'] = df['wins'] + df['losses'] + df['draws']
    
    # Changing the column location
    pop_column2 = df.pop('total_matches')
    df.insert(4, 'total_matches', pop_column2)
    print(df.head())

    print('-'*120)

    # Manchester United Season
    mu_season = utils.season_2017_2018
    print(mu_season)

if __name__ == '__main__':
    main()


  


