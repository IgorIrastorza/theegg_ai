# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:22:35 2022

@author: igori
"""

import re
import pandas as pd


def main():
    # Función principal del script.

    # Se lee el csv guardado en el repositorio de la tarea.
    df = pd.read_csv('poblacion_global_2020.csv')
    print(df.info())
    df = build_data(df)
    print('------------------------------------------------------------------')
    print(df.info())
    df_descr(df)


def build_data(df):
    # Función para estructurar correctamente el dataset para el procesado.

    # Se da formato a las filas nulas y columnas númericas.
    df['Tasa Fertilidad'] = df['Tasa Fertilidad'].replace(['N.A.'],
                                                          [float('nan')])
    df['Tasa Fertilidad'] = df['Tasa Fertilidad'].astype(float)

    df['Edad Promedio'] = df['Edad Promedio'].replace(['N.A.'], [float('nan')])
    df['Edad Promedio'] = df['Edad Promedio'].astype(float)

    df['% Poblacion Urbaba'] = df['% Poblacion Urbaba'].replace(['N.A.'],
                                                                [float('nan')])

    # Se usa Regex para quitar el string '%' y convertir todo a tipo float.
    pattern = re.compile('[0-9]{1,2}')
    for i in range(len(df['% Poblacion Urbaba'])):
        try:
            search_result = pattern.findall(df.iloc[i, 7])
            df.iloc[i, 7] = float(search_result[0])
        except TypeError:
            continue

    # Renombrar la columna de población urbana.
    df['% Poblacion Urbaba'] = df['% Poblacion Urbaba'].astype(float)
    df.rename(columns={"% Poblacion Urbaba": "% Poblacion Urbana"},
              inplace=True)

    return df


def df_descr(df):
    # Función para responder a las preguntas formuladas en el enunciado.
    print('------------------------------------------------------------------')
    print('- Promedio de tasa de fertilidad global:',
          df['Tasa Fertilidad'].mean())
    print('- Pais con edad promedio más alta:',
          df.iloc[(df['Edad Promedio'].idxmax(axis=0)), 0])
    print('- Edad promedio más alta:', df['Edad Promedio'].max())
    print('- Pais con edad promedio más baja:',
          df.iloc[(df['Edad Promedio'].idxmin(axis=0)), 0])
    print('- Edad promedio más baja:', df['Edad Promedio'].min())
    print('- Mediana del porcentaje de población urbana (%):',
          df['% Poblacion Urbana'].median())

    # Nuevo posible indicador para comparar la calidad de vida global.
    print('- Top 10 Tasa de Migración más alta por paises:')
    print(df.nlargest(n=10, columns=['Tasa Migracion']))
    df['prueba'] = df['Poblacion (2020)']
    print()
    print('- Top 10 Tasa de Migración más baja por paises:')
    print(df.nsmallest(n=10, columns=['Tasa Migracion']))


if __name__ == '__main__':
    main()
