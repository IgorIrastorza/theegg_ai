# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:29:12 2021

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
    estadistica_descr(dataframe['Incidencia acumulada Araba'])
    estadistica_descr(dataframe['Incidencia acumulada Bizkaia'])
    estadistica_descr(dataframe['Incidencia acumulada Gipuzkoa'])


def data_format(dates_list):
    # Función para pasar el formato de la fecha de string a datetime.
    for i in range(len(dates_list)):
        dates_list[i] = datetime.strptime(dates_list[i], '%Y-%m-%dT%H:%M:%S%z')

    return dates_list


def build_data():
    # Función para construir el dataframe adecuado para explotarlo después.
    with open('JSON/covid19-pcr.json', encoding='utf-8') as file:
        data = json.load(file)

    x = data['byDate']
    dataframe = pd.DataFrame(columns=['Fecha', 'Total positivos',
                                      'Incidencia acumulada Total',
                                      'Incidencia acumulada Araba',
                                      'Incidencia acumulada Bizkaia',
                                      'Incidencia acumulada Gipuzkoa'],
                             index=range(len(x)))

    for i in range(len(x)):
        dataframe.iloc[i] = [x[i]['date'], x[i]['positiveCount'],
                             x[i]['aggregatedIncidence'],
                             x[i]['aggregatedIncidenceAR'],
                             x[i]['aggregatedIncidenceBIZ'],
                             x[i]['aggregatedIncidenceGI']]

    dataframe['Fecha'] = data_format(dataframe['Fecha'])

    return dataframe


def plot(dataframe):
    # Función para diseñar y guardar las gráficas que nos interesan.
    dataframe.plot(kind='line', x='Fecha', y=['Incidencia acumulada Araba',
                                              'Incidencia acumulada Bizkaia',
                                              'Incidencia acumulada Gipuzkoa'],
                   label=["Araba", "Bizkaia", "Gipuzkoa"],
                   figsize=(10, 6), color=["Blue", "Green", "Orange"],
                   title='Evolución de la incidencia por región en la CAV',
                   xlabel='Fecha', ylabel='IA 14d casos / 100.000 hab',
                   fontsize=10, rot=0)

    plt.savefig('Graphics/graph3.png')

    dataframe.plot.box(y=['Incidencia acumulada Araba',
                          'Incidencia acumulada Bizkaia',
                          'Incidencia acumulada Gipuzkoa'],
                       label=["Araba", "Bizkaia", "Gipuzkoa"],
                       ylabel='IA 14d casos / 100.000 hab',
                       title='Evolución de la incidencia por región en la CAV',
                       figsize=(10, 6), fontsize=10, rot=0)

    plt.savefig('Graphics/graph4.png')

    dataframe.plot(kind='line', x='Fecha', y='Total positivos',
                   figsize=(10, 6),
                   title='Evolución de los casos positivos en la CAV',
                   xlabel='Fecha', ylabel='Número de casos diarios',
                   fontsize=10, rot=0)

    plt.savefig('Graphics/graph5.png')


def estadistica_descr(data_list):
    # Función para calcular los datos estadísticos principales de...
    # ... una lista de datos.
    print(data_list.name.upper())
    print()
    print('- Promedio:', data_list.mean())
    print('- Mediana:', data_list.median())
    print('- Cuartil inferior', data_list.quantile([0.25]))
    print('- Cuartil superior', data_list.quantile([0.75]))
    print('- Máximo:', data_list.max())
    print('- Mínimo:', data_list.min())
    print('------------------------------------------------------------------')


if __name__ == '__main__':
    main()
