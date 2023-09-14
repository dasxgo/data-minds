import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/home/dasxgo/dev/data-minds/reports/02-bike.csv')
print(df.head())

# Are there any specific time periods with higher/lower bike rental counts?

bike_count_avg = df.groupby(['hour'])['count'].mean().reset_index(name='avg_rides')

plt.figure(figsize=(14,8))
plt.barh(y=bike_count_avg['hour'], width=bike_count_avg['avg_rides'])
plt.xlabel('Average bike rental count')
plt.ylabel('Hour of day')
plt.title('Hourly Bike rental counts')
plt.show()


