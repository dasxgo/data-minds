import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utils
import load
import main

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

# Plotting the top 10 teams with most wins

data1 = main.df_wld

teams = data1.index[:10]
wins = data1.wins[:10]
matches = data1.total_matches[:10]
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

# Plotting the top 10 teams with most losses

data2 = main.df_lost

lost_teams = data2.index[:10]
losses = data1.losses[:10]
total_matches = data1.total_matches[:10]
plt.figure(figsize=(8, 4))
plt.style.use('ggplot')
x_index2 = np.arange(len(lost_teams))
plt.bar(x_index2 - 0.25, losses, width = 0.5, label = 'Total losses')
plt.bar(lost_teams, total_matches, width = 0.35, label = 'Total Matches')
plt.ylabel('Total losses per total matches', size = 14, color = 'black')
plt.xlabel('Teams', size = 15, color = 'black')
plt.xticks(rotation = 'vertical', size = 12, color = 'black')
plt.yticks(color = 'black')
plt.legend(loc = 4, prop = {'size': 10})
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


 

    
