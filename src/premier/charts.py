import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utils
import load

def plot_goals_home(data):
    plt.xticks(rotation=90)
    sns.lineplot(x="season", y="home_goals", data=data)
    plt.show()

def plot_mudf(data):
    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=90)
    sns.barplot(x="season", y="goals", data=data)
    plt.show()

def plot_goals(data):
    plt.figure(figsize=(10, 6))
    plt.style.use('seaborn-poster')
    plt.xticks(rotation=90);
    sns.barplot(x="season",y="goals",data=data)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.style.use('seaborn-poster')
    plt.xticks(rotation=90);
    sns.barplot(x="goals",y="team",data=data)
    plt.show()
    
def plot_wins(data):
    teams = df2.index[:10]
    wins = df2.wins[:10]
    matches = df2.total_matches[:10]
    plt.figure(figsize=(8, 4))
    plt.style.use('ggplot')
    # using x_index so that the bars can be placed side by side
    x_index = np.arange(len(teams))
    plt.bar(x_index - 0.25, wins, width = 0.5, label = 'Total Wins')
    plt.bar(teams, matches, width = 0.35, label = 'Total Matches')
    plt.ylabel('Total Wins per total matches', size = 10)
    plt.xlabel('Teams', size = 10)
    plt.xticks(rotation = 'vertical', size = 12)
    plt.legend(loc = 4, prop = {'size': 10})
    plt.show()

if __name__ == '__main__':
    data_goals_home = utils.season_goals
    data_mudf = utils.mudf
    data_goals = load.df_stats
    data_top_wins = utils.df2
    
    plot_goals_home(data_goals_home)
    plot_mudf(data_mudf)
    plot_goals(data_goals)
    plot_wins(data_top_wins)

    
