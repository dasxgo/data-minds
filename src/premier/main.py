import pandas as pd
import numpy as np
import utils 
from read_csv import df_results, df_stats

def main():

    dfy = (df_results[['home_goals', 'away_goals']])
    print(dfy)

    print('='*120)
    print(df_stats[0:7])
    
    print('='*120)

    print(df_results.shape)
    print('='*120)
    print(df_results.dtypes)

if __name__ == '__main__':
    main()


  


