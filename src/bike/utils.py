import pandas as pd
import numpy as np
import load

df = load.data

def categorize_stations(df):
    spring = df[df['season']==0]
    autumn = df[df['season']==2]
    winter = df[df['season']==3]
    summer = df[df['season']==1]
    return spring, autumn, winter, summer

if __name__ == '__main__':
    spring_df, autumn_df, winter_df, summer_df = categorize_stations(df)


