import pandas as pd
import numpy as np

data = pd.read_csv('/home/dasxgo/dev/data-minds/data/london_merged.csv')

if __name__ == '__main__':
    print(data.head())
    print('-'*120)
    print(data.tail())
    print('-'*120)
    print(data.shape)
    print('-'*120)
    print(data.columns)
    print('='*120)

    


