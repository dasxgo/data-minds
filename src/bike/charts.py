import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/home/dasxgo/dev/data-minds/reports/02-bike.csv')
print(df.head())
print(df.shape)


if __name__ == '__main__':
    # Are there any specific time periods with higher/lower bike rental counts?
    bike_count_avg = df.groupby(['hour'])['count'].mean().reset_index(name='avg_rides')
    plt.figure(figsize=(14,8))
    plt.barh(y=bike_count_avg['hour'], width=bike_count_avg['avg_rides'])
    plt.xlabel('Average bike rental count')
    plt.ylabel('Hour of day')
    plt.title('Hourly Bike rental counts')
    plt.show()

    # What are the variations in bike rental across different seasons?
    grouped_seasons = df.groupby (['season'])['count'].sum().reset_index(name= 'ride_count')
    sns.set_style('whitegrid')
    plt.figure(figsize=(12,6))
    explode = (0.1, 0.1, 0.1, 0.1)
    plt.pie(grouped_seasons['ride_count'], labels = ['Spring', 'Summer', 'Autumn', 'Winter'], 
            explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Bike sharing w.r.t Seasons')
    plt.show()

    # How does the rental count change during holidays?
    holiday_rental = df['is_holiday'].value_counts()
    plt.figure(figsize=(6,6))
    explode = (0.1, 0.1)
    plt.pie(holiday_rental, labels = ['No Holiday', 'Holiday'], 
            explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Holidays vs Non Holidays')
    plt.show()

    # How does the rental count change during weekends?
    weekend_rental = df['is_weekend'].value_counts()
    plt.figure(figsize=(6,6))
    explode = (0.1, 0.1)
    plt.pie(weekend_rental, labels = ['Weekdays', 'Weekend'], 
            explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Weekend vs Weekday')
    plt.show()

    # How does the bike rental count vary with different weather conditions
    rentals_by_weather = df.groupby(['wheather'])['count'].sum().reset_index(name='ride_count')
    plt.figure(figsize=(14,6))
    sns.barplot(x='wheather', y='ride_count', data=rentals_by_weather)
    plt.xlabel('wheather')
    plt.ylabel('Count of bikes rented')
    plt.title('Rental count w.r.t weather conditions')
    plt.xticks(rotation=45)
    plt.show()s




