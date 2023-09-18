import pandas as pd
import numpy as np
import load

df = load.data1

top_scorers = df.groupby('season')['pts'].max()
top_scorers = top_scorers.reset_index().merge(df[['season', 'player_name', 'pts']], on=['season', 'pts'], how='left')

if __name__ == '__main__':
    for season in top_scorers['season'].unique():
        season_top_scorer = top_scorers[top_scorers['season'] == season]
        print(f"Season {season} Top Scorer: {season_top_scorer['player_name'].values[0]} - {season_top_scorer['pts'].values[0]} points")
        print('-'*120)
      
