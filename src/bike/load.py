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

# Datatypes of each columns

data.rename(columns={'cnt': 'count', 't1' : 'c_temp', 't2' : 'f_temp', 'hum' : 'humidity'}, inplace= True)

print(data)
print(data.dtypes)
print('-'*120)

# Missing value

print(data.isnull().sum())
print('-'*120)

# Save the DataFrame to a CSV file

route = '/home/dasxgo/dev/data-minds/reports/01-bike.csv'
data.to_csv(route, index=False)  
print(f'DataFrame save in {route}')
print('-'*120)




    


