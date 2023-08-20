import pandas as pd
import numpy as np

df_results = pd.read_csv('/home/dasxgo/dev/jupyter/data/results.csv', sep=',', header=0)  
df_stats = pd.read_csv('/home/dasxgo/dev/jupyter/data/stats.csv', sep=',', header=0)


if __name__ == '__main__':
    print(df_results.head())
    print('='*120)
    print(df_stats.head())















