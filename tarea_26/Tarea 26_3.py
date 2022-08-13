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
    estadistica_descr(dataframe['Fallecidos'])


def data_format(dates_list):
    # Función para pasar el formato de la fecha de string a datetime.
    for i in range(len(dates_list)):
        dates_list[i] = datetime.strptime(dates_list[i], '%Y-%m-%dT%H:%M:%S%z')

    return dates_list


def build_data():
    # Función para construir el dataframe adecuado para explotarlo después.
    with open('JSON/covid19-epidemic-status.json', encoding='utf-8') as file:
        data = json.load(file)

    with open('JSON/covid19-deceasedPeople'
              'Count.json', encoding='utf-8') as file:
        data1 = json.load(file)

    with open('JSON/covid19-pcr.json', encoding='utf-8') as file:
        data2 = json.load(file)

    dataframe = pd.DataFrame(columns=['Fecha', 'Ocupación UCI',
                                      'Ingresos hospital con PCR+',
                                      'Fallecidos',
                                      'Tasa R0', 'Total positivos'],
                             index=range(len(data['dates'])))

    dataframe['Fecha'] = data_format(data['dates'])
    dataframe['Ocupación UCI'] = data['icuPeopleCount']
    dataframe['Ingresos hospital con PCR+'] = data['newHospital'
                                                   'AdmissionsWithPCRCount']
    dataframe['Tasa R0'] = data['r0']

    # Las fechas entre data y data1 estan descuadrados.
    # Se eliminan las primeras 6 filas, ya que no aportan ningun dato.
    dataframe = dataframe.drop(range(0, 6), axis=0)
    dataframe.reset_index(inplace=True, drop=True)

    x = data1['byDate']
    for i in range(len(x)):
        dataframe.iloc[i, 3] = x[i]['deceasedCount']

    for i in range(len(data2['positiveCounts'])):
        dataframe.iloc[i, 5] = data2['positiveCounts'][i]

    return dataframe
dataframe.plot(y='Total positivos', x='Fecha',
                        title='Evolución de los casos positivos y la tasa R0'
                        ' en la CAV', figsize=(10, 6), fontsize=10)

def plot(dataframe):
    # Función para diseñar y guardar las gráficas que nos interesan.
    ax = 
    ax2 = dataframe.plot(secondary_y=True, y='Tasa R0', color='grey',
                         x='Fecha', ax=ax)
    plt.axhline(y=1, color='red', linestyle='dashed', linewidth=1)
    ax.set_ylabel('Número de casos positivos diarios')
    ax2.set_ylabel('Tasa R0')

    plt.savefig('Graphics/graph6.png')

    ax = dataframe.plot(y='Total positivos', x='Fecha', title='Evolución de'
                        ' los casos positivos y los fallecimientos en la CAV',
                        figsize=(10, 6), fontsize=10)
    ax2 = dataframe.plot(secondary_y=True, y='Fallecidos', color='orange',
                         x='Fecha', ax=ax)
    ax.set_ylabel('Número de casos positivos diarios')
    ax2.set_ylabel('Número de fallecidos diarios')

    plt.savefig('Graphics/graph7.png')

    ax = dataframe.plot(y='Ocupación UCI', x='Fecha', color='green',
                        title='Evolución de la ocupación en UCIs y los'
                        ' fallecimientos en la CAV',
                        figsize=(10, 6), fontsize=10)
    ax2 = dataframe.plot(secondary_y=True, y='Fallecidos', color='orange',
                         x='Fecha', ax=ax)
    ax.set_ylabel('Ocupación UCI')
    ax2.set_ylabel('Número de fallecidos diarios')

    plt.savefig('Graphics/graph8.png')

    ax = dataframe.plot(y='Total positivos', x='Fecha', title='Evolución de'
                        ' los casos positivos y la ocupación en UCIs'
                        ' en la CAV', figsize=(10, 6), fontsize=10)
    ax2 = dataframe.plot(secondary_y=True, y='Ocupación UCI', color='green',
                         x='Fecha', ax=ax)
    ax.set_ylabel('Número de casos positivos diarios')
    ax2.set_ylabel('Ocupación UCI')
    plt.savefig('Graphics/graph9.png')


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
