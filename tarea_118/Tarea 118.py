# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 19:11:19 2022

@author: igori
"""


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import statsmodels.api as sm  # paquete estadístico parecido a R
import plotly.express as px  # crear gráficos interactivos
import plotly.io as pio
import plotly.figure_factory as ff  # crear figuras especiales de plotly
import scipy.stats as stats
import plotly.graph_objects as go
pio.renderers.default = 'browser'


def main():
    data = dataframe()
    carseats = sm.datasets.get_rdataset("Carseats", "ISLR")
    data.read_df(carseats.data)
    print(carseats.__doc__)
    data.build_data()
    data.descr_cuant()
    data.descr_uni_cuant()
    data.descr_uni_cual()
    data.descr_mult_cuant()
    data.descr_mult_cual()
    data.descr_mult_cualcuant()


class dataframe:
    def __init__(self):
        self.df = []
        self.__df_descrip = []
        self.__data_type = []
        self.__var_num = []
        self.__var_cual = []

    def read_df(self, df):
        self.__df = df

    def build_data(self):
        self.__df['HighSales'] = np.where(self.__df['Sales'] > 8, True, False)
        print(self.__df.info())
        #  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html
        self.__data_type = self.__df.dtypes
        self.__var_num = self.__data_type[
            (self.__data_type == 'int64') | (self.__data_type == 'float64')]
        self.__var_num = self.__var_num.index
        self.__var_cual = self.__data_type[
            (self.__data_type == 'object') | (self.__data_type == 'bool')]
        self.__var_cual = self.__var_cual.index

    def descr_cuant(self):
        # Descripción cuantitativa de todo el dataframe.

        # Media y Mediana
        media = pd.Series((self.__df[self.__var_num].mean()), name='mean')
        median = pd.Series((self.__df[self.__var_num].median()), name='median')
        self.__df_descrip = pd.merge(media, median, right_index=True,
                                     left_index=True)

        # Test de normalidad (Shapiro-Wilk test)
        # si pvalue > 0,05, sigue dist. normal (=no se puede decir que no siga)
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
        statvalue, pvalue = [], []
        for i in range(len(self.__var_num)):
            statvalue.append(stats.shapiro(
                self.__df[self.__var_num[i]]).statistic)
            pvalue.append(stats.shapiro(self.__df[self.__var_num[i]]).pvalue)

        self.__df_descrip['S-W test value'], self.__df_descrip[
            'p value'] = statvalue, pvalue

        # Desviación estandar, cuartiles y rango intercuartílico (IQR)
        desv = self.__df[self.__var_num].std()
        q1 = self.__df[self.__var_num].quantile(0.25)
        q3 = self.__df[self.__var_num].quantile(0.75)
        iqr = q3-q1
        self.__df_descrip['Desviation'], self.__df_descrip[
            'Quartile 1'] = desv, q1
        self.__df_descrip['Quartile 3'], self.__df_descrip[
            'IQR range'] = q3, iqr
        self.__df[self.__var_num].quantile(np.arange(0, 1, 0.1))

        # Error estandar y intervalo confianza 95% (distr. normal)
        self.__df_descrip['n'] = len(self.__df)
        # Error estandar y límites de confianza de la distribución normal.
        # El calculo del Error Estandar presupone una distribución normal.
        self.__df_descrip['Standard Error'] = desv/np.sqrt(len(self.__df))
        self.__df_descrip['IC lower 95%'] = self.__df_descrip['mean']-(
            1.96*(self.__df_descrip['Standard Error']))
        self.__df_descrip['IC upper 95%'] = self.__df_descrip['mean']+(
            1.96*(self.__df_descrip['Standard Error']))

    def descr_uni_cuant(self):
        # Descripción de una variable cuantitativa

        # Histograma
        sns.displot(self.__df.Price, kde=True)
        plt.title('Carseats price histogram', fontsize=14)
        plt.show()
        fig = px.histogram(self.__df, x="Price",
                           title='Carseats price histogram')
        fig.show()

        # Boxplot
        sns.boxplot(data=self.__df, x="Price")
        plt.title('Carseats price histogram', fontsize=14)
        plt.show()
        fig = px.box(self.__df, x="Price", title='Carseats price boxplot',
                     color_discrete_sequence=['indianred'])
        fig.show()

        # Histograma de densidad
        sns.displot(self.__df, x="Price", kind="kde", bw_adjust=2)
        plt.title('Carseats price density histogram', fontsize=14)
        plt.show()
        hist_data = [self.__df['Price']]
        group_labels = ['Price']
        fig = ff.create_distplot(hist_data, group_labels)
        fig.show()

        # Violin Plot
        sns.violinplot(data=self.__df, x="Price")
        plt.title('Carseats price violin plot', fontsize=14)
        plt.show()
        fig = px.violin(self.__df, x="Price",
                        title='Carseats price violin plot')
        fig.show()

        # Boxplot + Stripchart
        sns.stripplot(data=self.__df, x="Price")
        plt.title('Carseats price stripchart', fontsize=14)
        plt.show()
        fig = px.box(self.__df, x="Price", points="all",
                     title='Carseats price boxplot + stripchart')
        fig.show()

        # Probability plot (normal distr.)
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html
        stats.probplot(self.__df['Price'], dist="norm", plot=plt)
        plt.show()

        # 4 subplots in one.
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
        fig, axs = plt.subplots(ncols=4, figsize=(10, 4))
        sns.kdeplot(
            data=self.__df, x='Price',
            fill=True, common_norm=False, palette="crest",
            alpha=.5, linewidth=0, ax=axs[0])
        sns.boxplot(data=self.__df, y='Price', ax=axs[1])
        sns.stripplot(data=self.__df, y='Price', ax=axs[2])
        sns.violinplot(data=self.__df, y='Price', ax=axs[3])
        # https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html
        fig.tight_layout()
        plt.show()

        # Subplots de cada una de las variables del dataframe.
        for i in self.__var_num:
            fig, axs = plt.subplots(ncols=4, figsize=(10, 4))
            sns.kdeplot(
               data=self.__df, x=i,
               fill=True, common_norm=False, palette="crest",
               alpha=.5, linewidth=0, ax=axs[0])
            sns.boxplot(data=self.__df, y=i, ax=axs[1])
            sns.stripplot(data=self.__df, y=i, ax=axs[2])
            sns.violinplot(data=self.__df, y=i, ax=axs[3])
            fig.tight_layout()
            plt.show()

    def descr_uni_cual(self):
        # Descripción de una variable cualitativa
        print('Tabla de frecuencias absolutas:')
        print(self.__df['ShelveLoc'].value_counts())
        print('Tabla de frecuencias porcentaje:')
        pct = self.__df['ShelveLoc'].value_counts(normalize=True)
        print(pct)
        sns.barplot(x=pct.index.tolist(), y=pct.values)
        plt.ylabel('Percentage')
        plt.title('Shelve location comparison by frequency', fontsize=14)
        plt.show()

        # Tabla y gráfico de frecuencias para cada variable
        for i in self.__var_cual:
            print('Tabla de frecuencias absolutas:')
            print(self.__df[i].value_counts())
            print('Tabla de frecuencias porcentaje:')
            pct = self.__df[i].value_counts(normalize=True)
            print(pct)
            sns.barplot(x=pct.index.tolist(), y=pct.values)
            plt.ylabel('Percentage')
            plt.title('%s comparison by frequency' % i, fontsize=14)
            plt.show()

        # Gráfico de frecuencias (conteo absoluto, sin porcentajes)
        pct = self.__df['ShelveLoc'].value_counts(normalize=False)
        sns.barplot(x=pct.index.tolist(), y=pct.values)
        plt.ylabel('Count')
        plt.title('Shelve location comparison by frequency', fontsize=14)
        plt.show()

        fig = px.bar(x=pct.index.tolist(), y=pct.values,
                     title='Shelve location comparison by frequency')
        fig.show()

        # Diagrama de sectores
        colors = sns.color_palette('pastel')[0:len(pct)]
        plt.pie(pct.values, labels=pct.index, colors=colors, autopct='%.0f%%')
        plt.title('Shelve location comparison by frequency', fontsize=14)
        plt.show()

        fig = px.pie(values=pct.values, names=pct.index,
                     title='Shelve location comparison by frequency')
        fig.show()
        fig = px.pie(values=pct.values, names=pct.index, hole=.3,
                     title='Shelve location comparison by frequency')
        fig.show()

    def descr_mult_cuant(self):
        # Descripción de varias variables cuantitativas

        # Diagrama de dispersión
        sns.scatterplot(data=self.__df, x=self.__df.Price, y=self.__df.Sales)
        plt.title('Price-Sales scatterplot', fontsize=14)
        plt.show()
        fig = px.scatter(self.__df, x=self.__df.Price, y=self.__df.Sales,
                         title='Price-Sales scatterplot')
        fig.show()

        # Diagrama de dispersión 3D
        fig = px.scatter_3d(self.__df, x=self.__df.Sales,
                            y=self.__df.CompPrice, z=self.__df.Price,
                            size_max=0.1,
                            title='Sales-CompPrice-Price 3D scatterplot',
                            color=self.__df.ShelveLoc)
        fig.update_traces(marker_size=3)
        fig.show()

        # Matrixplot
        sns.pairplot(self.__df[self.__var_num])
        plt.show()
        fig = px.scatter_matrix(self.__df[self.__var_num])
        fig.show()

        # Correlogram
        # Increase the size of the heatmap.
        plt.figure(figsize=(16, 6))
        # Set the range of values to be displayed on the colormap from -1 to 1
        # Set annot to True to display the correlation values on the heatmap.
        heatmap = sns.heatmap(self.__df[self.__var_num].corr(), vmin=-1,
                              vmax=1, annot=True)
        # Pad defines the distance of the title from the top of the heatmap.
        heatmap.set_title('Correlation Heatmap', fontdict={'fontsize': 12},
                          pad=12)
        plt.show()

        fig = px.imshow(self.__df[self.__var_num].corr(), aspect="auto",
                        title='Correlation Heatmap')
        fig.show()

    def descr_mult_cual(self):
        # Descripción de varias variables cualitativas

        # Diagrama de frecuencias absolutas
        sns.countplot(x=self.__df.HighSales, hue=self.__df.ShelveLoc)
        plt.title('High sales depending on shelve location', fontsize=14)
        plt.show()
        print(pd.DataFrame(self.__df[['HighSales',
                                      'ShelveLoc']].value_counts()))
        print(pd.DataFrame(self.__df[['HighSales', 'ShelveLoc']].value_counts(
            normalize=True)))

    def descr_mult_cualcuant(self):
        # Análisis multivariada entre variables cuantitativas y cualitativas

        # Histograma de densidad
        sns.kdeplot(x=self.__df.Sales, hue=self.__df.ShelveLoc, fill=True,
                    common_norm=False, alpha=.5, linewidth=0)
        plt.show()

        # Matrixplot
        fig = px.scatter_matrix(self.__df, dimensions=self.__var_num,
                                color=self.__df.HighSales,
                                title='Matrixplot for high sales groups')
        fig.show()

        # Bubble plot
        fig = px.scatter(x=self.__df.Price, y=self.__df.Sales,
                         size=self.__df.Population, color=self.__df.ShelveLoc,
                         hover_name=self.__df.Urban, size_max=10,
                         title='Bubble plot')
        fig.show()

        # Radar plot
        id_vars = [6, 9, 10, 11]
        data_melt = pd.melt(self.__df, id_vars=self.__df.columns[id_vars])

        data_melt['Quartile'] = data_melt.groupby(
            ['variable'])['value'].rank(method='max').copy()
        data_melt['Ranking'] = data_melt['Quartile']
        data_melt['Ranking'] = max(data_melt['Ranking'])-data_melt['Ranking']+1
        data_melt['Quartile'] = data_melt.groupby(
            ['variable'])['value'].rank(method='min',
                                        pct=True).round(2).copy()*100
        data_melt['index'] = np.tile(np.arange(len(self.__df)),
                                     len(self.__var_num))

        data_percentiles = data_melt.pivot(index='index', columns='variable',
                                           values="Quartile")
        data_percentiles = data_percentiles.reset_index()
        data_percentiles.columns.name = None

        i = 0  # tienda de la fila uno
        j = 1  # tienda de la fila dos

        # Compararemos las dos tiendas en las siguientes variables:
        categories = ['Sales', 'CompPrice', 'Price', 'Income', 'Education',
                      'Advertising', 'Age', 'Population']

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
              r=data_percentiles[categories].iloc[i, :],
              theta=categories,
              fill='toself',
              name='Tienda nº '+str(data_percentiles.index[i])
        ))
        fig.add_trace(go.Scatterpolar(
              r=data_percentiles[categories].iloc[j, :],
              theta=categories,
              fill='toself',
              name='Tienda nº '+str(data_percentiles.index[j])
        ))

        fig.update_layout(
          polar=dict(
            radialaxis=dict(
              visible=True
              # ,range=[0, 5]
            )),
          showlegend=True
        )

        fig.show()


if __name__ == '__main__':
    main()
