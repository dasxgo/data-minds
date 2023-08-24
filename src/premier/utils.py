import pandas as pd
import numpy as np
from load import df_results, df_stats

# Manchester United

mudf = df_stats['team'] == "Manchester United"
mudf = df_stats[mudf]

season = mudf.groupby('season').sum()

season_2017_2018 = season.loc['2017-2018']

season_goals = df_results.groupby('season').sum(['home_goals', 'away_goals'])

tm=df_stats.groupby(['team'])
tm=tm['penalty_save'].agg('max')
tm=pd.DataFrame(tm)
tm.reset_index(drop=False,inplace=True)
tm.set_index('penalty_save',inplace=True)
tm.sort_index(ascending=False)
tm.reset_index(drop=False,inplace=True)
tm=tm.nlargest(15,"penalty_save")

tm2=df_stats.groupby(['team'])
tm2=tm2['touches'].agg('max')
tm2=pd.DataFrame(tm2)
tm2.reset_index(drop=False,inplace=True)
tm2.set_index('touches',inplace=True)
tm2.sort_index(ascending=False)
tm2.reset_index(drop=False,inplace=True)
tm2=tm2.nlargest(15,"touches")

yel=df_stats.groupby('team').total_yel_card.mean()
yel=pd.DataFrame(yel)
yel.sort_values('total_yel_card',ascending=False,inplace=True)

red=df_stats.groupby('team').total_red_card.mean()
red=pd.DataFrame(red)
red.sort_values('total_red_card',inplace=True)


if __name__ == '__main__':
    print('Team: Manchester United')
    print('='*160)
    print(season)
    print('-'*160)
    print(season_goals)
    print('-'*160)
    print(f' minimun goals season Manchester United => ', season['goals'].min())
    print('-'*160)
    print(season_2017_2018)
    print('-'*160)
    print(tm) 
    print('-'*160)
    print(df_wld.head(10))
    
    
   