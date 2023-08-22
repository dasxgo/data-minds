import pandas as pd
import numpy as np
from read_csv import df_results, df_stats

# Manchester United

mudf = df_stats['team'] == "Manchester United"
mudf = df_stats[mudf]

season = mudf.groupby('season').sum()

season_2017_2018 = season.loc['2017-2018']

season_goals = df_results.groupby('season').sum(['home_goals', 'away_goals'])

if __name__ == '__main__':
    print(season)
    print('-'*120)
    print(season_goals)
    print('-'*120)
    print(f' minimun goals season Manchester United => ', season['goals'].min())
    print('-'*120)
    print(season_2017_2018)
    print('-'*120)
   