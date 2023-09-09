import pandas as pd
import numpy as np

df = pd.read_csv('/home/dasxgo/dev/data-minds/reports/01-bike.csv')

def categorize_stations(df):
    spring = df[df['season']==0]
    autumn = df[df['season']==2]
    winter = df[df['season']==3]
    summer = df[df['season']==1]
    return spring, autumn, winter, summer

if __name__ == '__main__':
    spring_df, autumn_df, winter_df, summer_df = categorize_stations(df)
    print(spring_df)
    print('-'*120)
    print(autumn_df)
    print(f' Maximun autumn count =>',autumn_df['count'].max())
    print('-'*120)
    print(winter_df)
    print(f'Minimum winter count =>', winter_df['count'].min())
    print('-'*120)
    print(summer_df)
    print('-'*120)

