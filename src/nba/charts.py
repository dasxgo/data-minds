import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import load
import random

df = load.data1

if __name__ == '__main__':
    random_player = random.choice(df['player_name'])
    player_data = df[df['player_name'] == random_player]
    plt.plot(player_data['season'], player_data['pts'], label='Points')
    plt.plot(player_data['season'], player_data['reb'], label='Rebounds')
    plt.plot(player_data['season'], player_data['ast'], label='Assists')
    plt.xlabel('Season')
    plt.ylabel('Stats')
    plt.title(f'{random_player} Performance Over Time: Points, Rebounds, and Assists')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

    michael_jordan = df[df['player_name'] == 'Michael Jordan']
    print(michael_jordan)
    plt.plot(michael_jordan['season'], michael_jordan['pts'], label='Points')
    plt.plot(michael_jordan['season'], michael_jordan['reb'], label='Rebounds')
    plt.plot(michael_jordan['season'], michael_jordan['ast'], label='Assists')
    plt.xlabel('Season')
    plt.ylabel('Stats')
    plt.title(f'Michael Jordan Performance Over Time: Points, Rebounds, and Assists')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

    lebron_james = df[df['player_name'] == 'LeBron James']
    print(lebron_james)
    plt.plot(lebron_james['season'], lebron_james['pts'], label='Points')
    plt.plot(lebron_james['season'], lebron_james['reb'], label='Rebounds')
    plt.plot(lebron_james['season'], lebron_james['ast'], label='Assists')
    plt.xlabel('Season')
    plt.ylabel('Stats')
    plt.title(f'LeBron James Performance Over Time: Points, Rebounds, and Assists')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

    kobe_bryant = df[df['player_name'] == 'Kobe Bryant']
    print(kobe_bryant)
    plt.plot(kobe_bryant['season'], kobe_bryant['pts'], label='Points')
    plt.plot(kobe_bryant['season'], kobe_bryant['reb'], label='Rebounds')
    plt.plot(kobe_bryant['season'], kobe_bryant['ast'], label='Assists')
    plt.xlabel('Season')
    plt.ylabel('Stats')
    plt.title(f'Kobe Bryant Performance Over Time: Points, Rebounds, and Assists')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
  
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subchart
    plt.plot(michael_jordan['season'], michael_jordan['pts'], label='Points')
    plt.plot(michael_jordan['season'], michael_jordan['reb'], label='Rebounds')
    plt.plot(michael_jordan['season'], michael_jordan['ast'], label='Assists')
    plt.xlabel('Season')
    plt.ylabel('Stats')
    plt.title('Michael Jordan Performance')
    plt.legend()
    plt.xticks(rotation=45)
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subchart
    plt.plot(lebron_james['season'], lebron_james['pts'], label='Points')
    plt.plot(lebron_james['season'], lebron_james['reb'], label='Rebounds')
    plt.plot(lebron_james['season'], lebron_james['ast'], label='Assists')
    plt.xlabel('Season')
    plt.ylabel('Stats')
    plt.title('LeBron James Performance')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    










