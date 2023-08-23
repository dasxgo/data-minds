import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utils
import read_csv

def plot_season_goals(data):
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

    plt.figure(figsize=(15, 12))
    plt.style.use('seaborn-poster')
    plt.xticks(rotation=90);
    sns.barplot(x="goals",y="team",data=data)
    plt.show()

if __name__ == '__main__':
    data_season_goals = utils.season_goals
    data_mudf = utils.mudf
    data_goals = read_csv.df_stats
    
    plot_season_goals(data_season_goals)
    plot_mudf(data_mudf)
    plot_goals(data_goals)

    
