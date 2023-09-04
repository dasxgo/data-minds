import pandas as pd
import numpy as np

df = pd.read_csv('/home/dasxgo/dev/data-minds/data/london_merged.csv')

if __name__ == '__main__':
    print(df.head())
    print('-'*120)
    print(df.tail())
    print('-'*120)
    print(df.shape)
    print('-'*120)
    print(df.columns)

    print('='*120)

    # Remaning some of columns
    df.rename(columns={'cnt': 'count', 't1' : 'c_temp', 't2' : 'f_temp', 'hum' : 'humidity'}, inplace= True)
    print(df.columns)
    print('-'*120)

    # Datatypes of each columns
    print(df.dtypes)
    print('-'*120)

    # Missing value
    print(df.isnull().sum())

    # Save the DataFrame to a CSV file

    route = '/home/dasxgo/dev/data-minds/reports/01-bike.csv'
    df.to_csv(route, index=False)  
    print(f'DataFrame save in {route}')