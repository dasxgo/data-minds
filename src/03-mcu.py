import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from main import df_results, df_stats

if __name__ == '__main__':
    mudf = df_stats['team'] == "Manchester United"
    mudf = df_stats[mudf]

    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=90)
    sns.barplot(x="season",y="goals",data=mudf)
    plt.show()