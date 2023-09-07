import pandas as pd
import numpy as np
import load

df = load.data

def main():
    # Remaning some of columns
    df.rename(columns={'cnt': 'count', 't1' : 'c_temp', 't2' : 'f_temp', 'hum' : 'humidity'}, inplace= True)
    print(df.columns)
    print('-'*120)

    # Datatypes of each columns
    print(df.dtypes)
    print('-'*120)

    # Missing value
    print(df.isnull().sum())
    print('-'*120)

    # Save the DataFrame to a CSV file

    route = '/home/dasxgo/dev/data-minds/reports/01-bike.csv'
    df.to_csv(route, index=False)  
    print(f'DataFrame save in {route}')
    print('-'*120)

    # Feature Engineering 4 new columns from timestamp column and also weather_code

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['year'] = df['timestamp'].dt.year
    df['day'] = df['timestamp'].dt.day_name()
    df['hour'] = df['timestamp'].dt.hour
    df['week'] = df['timestamp'].dt.isocalendar().week

    weather_dict = {1: 'clear', 2: 'Scattered Clouds', 3: 'Broken Clouds',
                     4: 'Cloudy', 7: 'Rain', 10: 'Rain with Thunderstorm',
                     26: 'Showfall'}
    df['wheather'] = df['weather_code'].map(weather_dict)

    # Daily average bike shares per season

    grouped_season_avg = ((df.groupby(['season'])['count'].mean())*24).reset_index()
    print(grouped_season_avg)
    print('-'*120)

    # The number of bikes shares when the weather is hottest

    hottest = df[df['c_temp'] == df['c_temp'].max()]
    print(hottest)
    print('-'*120)

    # The number of bike shares when weather is coldest

    coldest = df[df['c_temp'] == df['c_temp'].min()]
    print(coldest)
    print('-'*120)

    # The number of bike shares when the wind speed is highest

    highest = df[df['wind_speed'] == df['wind_speed'].max()]
    print(highest)
    print('-'*120)

    # Season

    spring = df[df['season']==0]
    autumn = df[df['season']==2]
    winter = df[df['season']==3]
    summer = df[df['season']==1]

    # Lowest number of bikes shares in winter

    print(winter[winter['count']==winter['count'].min()])
    print('-'*120)

    # Highest number of bike share in autumn or fall

    print(autumn[autumn['count']==autumn['count'].max()])
    print('-'*120)

    # How is the bike rental demand distributed over weeks 

    ride_count_year = df.groupby(['year'])['count'].sum().reset_index(name='ride count')
    print(ride_count_year)
    print('-'*120)

    # How is the bike rental demand distributed over weeks

    weekly_ride_count = df.groupby(['week'])['count'].sum().reset_index(name='ride count')
    print(weekly_ride_count.head(13)) 
    print('-'*120)

if __name__ == '__main__':
    main()




