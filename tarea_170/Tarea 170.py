# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:16:19 2022

@author: igori
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = data()
    plot(df)


def data():
    df = pd.DataFrame(pd.read_csv('featuresdf.csv'))
    print(df.info())
    return df


def plot(df):
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
    # https://matplotlib.org/stable/api/pyplot_summary.html
    # https://seaborn.pydata.org/introduction.html
    # https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot
    # https://seaborn.pydata.org/generated/seaborn.violinplot.html

    ax = df.hist(column='danceability', bins=10, alpha=0.5, color='red',
                 legend=True)
    ax2 = df.hist(column='energy', alpha=0.5, ax=ax, legend=True)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Danceability and Energy histogram', fontsize=14)
    plt.show()

    sns.displot(data=[df.danceability, df.energy], kind='kde')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Danceability and Energy histogram', fontsize=14)
    plt.show()

    sns.distplot(df.danceability, bins=10, color='purple', kde=True)
    sns.distplot(df.energy, bins=10, color='blue', kde=True)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Danceability and Energy histogram', fontsize=14)
    plt.show()

    sns.violinplot(data=[df.danceability, df.energy])
    plt.ylabel('Valor')
    plt.legend(('Danceability', 'Energy'))
    plt.title('Danceability and Energy Violin diagram', fontsize=14)
    plt.show()

    sns.boxplot(data=df, x="danceability")
    plt.xlabel('Valor')
    plt.title('Danceability Box Plot', fontsize=14)
    plt.show()


if __name__ == '__main__':
    main()
