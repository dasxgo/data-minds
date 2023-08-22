import pandas as pd
import numpy as np

df_results = pd.read_csv('/home/dasxgo/dev/data-insights/data/results.csv', sep=',', header=0)  
df_stats = pd.read_csv('/home/dasxgo/dev/data-insights/data/stats.csv', sep=',', header=0)


if __name__ == '__main__':
    print(df_results.head())
    print('='*120)
    print(df_stats.head())

    print(df_results[['home_goals', 'away_goals']])
    print('='*120)
    print(df_stats[0:7])















