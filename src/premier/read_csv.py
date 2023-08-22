import pandas as pd
import numpy as np

df_results = pd.read_csv('/home/dasxgo/dev/data-insights/data/results.csv', sep=',', header=0)  
df_stats = pd.read_csv('/home/dasxgo/dev/data-insights/data/stats.csv', sep=',', header=0)


if __name__ == '__main__':
    # Results data
    print(df_results.head())
    print('-'*120)
    print(f'results shape => ', df_results.shape)
    print('-'*120)
    print(f'results index => ', df_results.index)
    print('-'*120)
    print(f'results columns => ', df_results.columns)
    print('-'*120)
    print(df_results.dtypes)
    print('-'*120)
    print(df_results.isnull().sum())
    
    print('='*120)

    
    # stats data
    print(df_stats.head())
    print('-'*120)
    print(f'stats shape => ', df_stats.shape)
    print('-'*120)
    print(f'stats index => ', df_stats.index)
    print('-'*120)
    print(f' stats columns => ', df_stats.columns)
    print('-'*120)
    print(df_stats.dtypes)
    print('-'*120)
    print(df_stats.isnull().sum())
    
    print('='*120)

    # Other data
    print(df_results[['home_goals', 'away_goals']])
    print('='*120)
    print(df_stats[0:7])















