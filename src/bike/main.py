import pandas as pd
import numpy as np
import load
from utils import categorize_stations

df = load.data

def main():
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

    spring_df, autumn_df, winter_df, summer_df = categorize_stations(df)

    # Lowest number of bikes shares in winter
    print(winter_df[winter_df['count']==winter_df['count'].min()])
    print(f'Minimum winter count =>', winter_df['count'].min())
    print('-'*120)

    # Highest number of bike share in autumn or fall
    print(autumn_df[autumn_df['count']==autumn_df['count'].max()])
    print(f'Maximun autumn count =>',autumn_df['count'].max())
    print('-'*120)

    # How is the bike rental demand distributed over weeks 

    ride_count_year = df.groupby(['year'])['count'].sum().reset_index(name='ride count')
    print(ride_count_year)
    print('-'*120)

    # How is the bike rental demand distributed over weeks

    weekly_ride_count = df.groupby(['week'])['count'].sum().reset_index(name='ride count')
    print(weekly_ride_count.head(13)) 
    print('-'*120)

    # How is the bike rental demand distribuyed over days

    count_per_day = df.groupby(['day'])['count'].sum().reset_index(name='ride count')
    print(count_per_day.sort_values(ascending=False, by='ride count'))
    print('-'*120)

    # How is the bike rental demand distributed over hours

    count_by_hour = df.groupby(['hour'])['count'].sum().reset_index(name='ride count')
    print(count_by_hour.sort_values(ascending=False, by='ride count'))
    print('-'*120)

    # Does the temperature have a a noticiable impact or bike?

    print(df[['count', 'c_temp', 'f_temp']].corr())
    print('-'*120)

    # Is there a correlation between bike rentals and wind speed, humidity or season 

    print(df[['count', 'wind_speed', 'humidity', 'season']].corr())
    print('-'*120)

    # Average Humidity in spring

    avg_humidity = round(spring_df['humidity'].mean(),2)
    print(f'The average Humidity in the spring is => {avg_humidity}')

    # Save the DataFrame to a CSV file
 
    route = '/home/dasxgo/dev/data-minds/reports/02-bike.csv'
    df.to_csv(route, index=False)  
    print(f'DataFrame save in {route}')
    print('-'*120)

    print(df.head())
    print(df.shape)
    
if __name__ == '__main__':
    main()






