import pandas as pd
import numpy as np
from main import df_results, df_stats

if __name__ == '__main__':
    print(df_results[['home_goals', 'away_goals']])
    print('='*120)
    print(df_stats[0:7])
    
    print('='*120)

    print(df_results.shape)
    print('='*120)
    print(df_results.dtypes)


  


