import pandas as pd
import numpy as np
import utils
import load
from load import df_stats

def main():

    df = load.df_stats
 
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

    # Creating a new column draw
    df['draws'] = 38 - df['wins'] - df['losses']
    # Changing the column location
    pop_column = df.pop('draws')
    df.insert(3, 'draws', pop_column)
    # Creating a new column total_matches
    df['total_matches'] = df['wins'] + df['losses'] + df['draws']
    #Changing the column location
    pop_column2 = df.pop('total_matches')
    df.insert(4, 'total_matches', pop_column2)
    print(df.head())

    print('-'*120)

if __name__ == '__main__':
    main()

# Creating a new column draws
df_stats['draws'] = 38 - df_stats['wins'] - df_stats['losses']
# Changing the column location
pop_column = df_stats.pop('draws')
df_stats.insert(3, 'draws', pop_column)
# Creating a new column total_matches
df_stats['total_matches'] = df_stats['wins'] + df_stats['losses'] + df_stats['draws']
# Changing the column location
pop_column2 = df_stats.pop('total_matches')
df_stats.insert(4, 'total_matches', pop_column2)
print(df_stats.head())

print('-'*120)

# Creating a new dataframe to find the total wins, losses, draws, total_matches by grouping teams
df_wld = df_stats.groupby('team').agg({'wins':'sum', 'losses':'sum', 'draws':'sum', 'total_matches':'sum'})
# Sorting the teams with most wins and getting the top 10 teams
df_wld = df_wld.sort_values(by = 'wins', ascending = False)
print(df_wld.head(10))

print('-'*120)

# Finding the teams with most losses

df_lost = df_wld.sort_values(by = 'losses', ascending = False)
print(df_lost.head(10))


  


