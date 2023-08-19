import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from main import df_results, df_stats

if __name__ == '__main__':
    season_goals = df_results.groupby('season').sum(['home_goals', 'away_goals'])
    print(season_goals)

    print('='*120)

    plt.xticks(rotation=90);
    sns.lineplot(x="season",y="home_goals",data=season_goals)
    plt.show()

    