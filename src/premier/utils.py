import pandas as pd
import numpy as np
from read_csv import df_results, df_stats


mudf = df_stats['team'] == "Manchester United"
mudf = df_stats[mudf]

season_goals = df_results.groupby('season').sum(['home_goals', 'away_goals'])

if __name__ == '__main__':
    print(season_goals)