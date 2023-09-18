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



