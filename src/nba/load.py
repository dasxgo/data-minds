import pandas as pd
import numpy as np

data = pd.read_csv('/home/dasxgo/dev/data-minds/data/all_seasons.csv')

if __name__ == '__main__':
    print(data.head())
    print('-'*120)
    print(data.shape)
    print('-'*120)
    print(data.tail())
    print('-'*120)
    print(data.columns)
    print('-'*120)
    print(data['season'].max())

    # Data types for columns
    print(data.dtypes)
    print('-'*120)

    # Missing values
    print(data.isnull().sum())
    print('-'*120)

# Delete column
df = (data.drop('college', axis=1))
print(df)
print('-'*120)
print(df.dtypes)
print('-'*120)
print(df.isnull().sum())
