import pandas as pd
import matplotlib.pyplot as plt
import statistics

def denirostats(file):
    df=pd.read_csv(file)
    sumstats=pd.DataFrame({'Mean Score':round(df.iloc[:,1].mean(),2),
                           'Median Score':round(df.iloc[:,1].median(),2),
                           'Standard Deviation of Scores':round(statistics.stdev(df.iloc[:,1]),2)},
                           index=[0])
    return sumstats

def denirohist(file):
    df=pd.read_csv(file)
    plt.hist(df.iloc[:,1],bins=[0,10,20,30,40,50,60,70,80,90,100],edgecolor='black')
    plt.title("Rotten Tomatoes Score Distribution of Robert De Niro Movies")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()

print(denirostats('deniro.csv'))
denirohist('deniro.csv')
