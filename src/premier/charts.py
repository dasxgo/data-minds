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

def plot_penalty_save(data):
    plt.xticks(rotation=90);
    sns.scatterplot(x="team",y="penalty_save",data=data)
    plt.show()

def plot_touch_team(data):
    plt.xticks(rotation=90);
    sns.scatterplot(x="team",y="touches",data=data)
    plt.show() 

def plot_yellow_card(data):
    sns.heatmap(data,cmap="Wistia_r")
    plt.show()

def plot_red_card(data):
    sns.heatmap(data,cmap="Reds")
    plt.show()
    
if __name__ == '__main__':
    data_goals_home = utils.season_goals
    data_mudf = utils.mudf
    data_goals = load.df_stats
    data_penalty_save = utils.tm
    data_touch_team = utils.tm2
    data_yellow_card = utils.yel
    data_red_card = utils.red
        
    plot_goals_home(data_goals_home)
    plot_mudf(data_mudf)
    plot_goals(data_goals)
    plot_penalty_save(data_penalty_save)
    plot_touch_team(data_touch_team)
    plot_yellow_card(data_yellow_card)
    plot_red_card(data_red_card)


 

    
