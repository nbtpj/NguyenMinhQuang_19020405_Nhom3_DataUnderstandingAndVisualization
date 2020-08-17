import json
import pandas as pd
import matplotlib.pyplot as plt
def main(file):
    f = open(file, encoding='utf-8', mode = 'r')
    p = pd.read_csv(f)
    # get data from file, store data frame to p value

    rate = p['rate'].value_counts(sort=True, normalize=True, dropna=False)
    price = p['price'].value_counts(dropna=False, bins=5)
    # get 2 column from data frame stored in p


    rate.plot.bar(color='green')
    plt.title('rate frequency')
    plt.xlabel('/5')
    plt.ylabel('amount')
    plt.show()
    price.plot.bar(price, color='orange')
    plt.title('price range')
    plt.xlabel('$')
    plt.ylabel('amount')
    plt.show()
    # visualization

main('amazon_1.csv')
