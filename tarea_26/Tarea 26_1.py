# -*- coding: utf-8 -*-
"""
Created on Wed Jul 7 20:06:15 2021

@author: igori
"""
import pandas as pd
import json
import matplotlib.pyplot as plt
from datetime import datetime
plt.rcParams.update({'figure.max_open_warning': 0})


def main():
    dataframe = build_data()
    plot(dataframe)


def data_format(dates_list):
    # Función para pasar el formato de la fecha de string a datetime.
    for i in range(len(dates_list)):
        dates_list[i] = datetime.strptime(dates_list[i], '%Y-%m-%dT%H:%M:%S%z')

    return dates_list


def build_data():
    # Función para construir el dataframe adecuado para explotarlo después.
    with open('JSON/covid19-pcr-positives.json') as file:
        data = json.load(file)

    del data['lastUpdateDate'], data['name'], data['metaData']

    dataframe = pd.DataFrame.from_dict(data, orient='columns')
    dataframe = dataframe.drop(dataframe.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                  10, 11, 12, 13]],
                               axis='columns')

    dataframe['dates'] = data_format(dataframe['dates'])

    return dataframe


def plot(dataframe):
    # Función para diseñar y guardar las gráficas que nos interesan.
    dataframe.plot(kind='line', x='dates', y=['menCount', 'womenCount'],
                        figsize=(10, 6), label=["Hombres", "Mujeres"],
                        color=["DarkBlue", "DarkGreen"],
                        title='Evolución de los casos COVID-19 por sexo en la'
                        ' CAV', xlabel='Fecha', ylabel='Número de casos',
                        fontsize=10, rot=0)
    plt.savefig('Graphics/graph0.png')

    dataframe.plot.area(colormap="Paired", x='dates', y=[3, 4, 5, 6, 7, 8,
                                                         9, 10, 11, 12],
                        figsize=(14, 10),
                        title='Evolución de los casos COVID-19 por edad en la'
                        ' CAV', xlabel='Fecha', ylabel='Número de casos',
                        fontsize=10, rot=0)
    plt.savefig('Graphics/graph1.png')
    dataframe.plot(subplots=True, x='dates', y=[3, 4, 5, 6, 7, 8,
                                                9, 10, 11, 12],
                   figsize=(14, 20),
                   title='Evolución de los casos COVID-19 por edad en la CAV',
                   xlabel='Fecha', ylabel='Número de casos')
    plt.savefig('Graphics/graph2.png')


if __name__ == '__main__':
    main()
