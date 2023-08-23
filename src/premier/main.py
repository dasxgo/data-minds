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
    print('='*120)

if __name__ == '__main__':
    main()


  


