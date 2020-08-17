import pandas as pd
import json as js
import matplotlib.pyplot as plt
import datetime as dt

def main(file):
    f = open(file, encoding='utf-8', mode='r')
    p = pd.read_csv(f)
    # get data from file then store to p value

    p = p.sort_values(by='time')
    # sort data frame stored in d by the value of column time

    a = []
    for set in p['tag'][:-200]:
        set = set.replace('[', '')
        set = set.replace(']', '')
        for x in set.split(','):
            a.append(x)
    top_tag = pd.Series(a)
    # get data in the last 200 row of data frame (sorted), stored them to a new set top_tag

    top_tag = top_tag.value_counts(sort = True,normalize=True,)
    # make a new table counting the frequency of each key word in top_tag, store them back to top_tag

    top_tag[:10].plot.bar(color='green')
    plt.xlabel('key_word', color='red')
    plt.ylabel('frequency', color='orange')
    plt.title('top key words on ' + str(file).split('.')[0])
    plt.show()
    # visualization

    print(top_tag[:10])
    # for checking the result
main('vietnamnet.csv')
main('vnexpress.csv')



