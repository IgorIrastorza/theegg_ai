# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:30:04 2022

@author: igori
"""

import pandas as pd

df = pd.read_csv('dataset/01_diabetes.csv')

# Renombrar todos los nombres de las columnas.
newcols = {"Pregnancies": "embarazo", "Glucose": "glucosa",
           "BloodPressure": "presion_sangre", "SkinThickness": "espesor_piel",
           "Insulin": "insulina", "BMI": "BMI",
           "DiabetesPedigreeFunction": "pedigree", "Age": "edad",
           "Outcome": "salida"}
# Pasamos un diccionario en columns y inplace=True para no crear un nuevo df.
df.rename(columns=newcols, inplace=True)
df.shape  # Número de filas y columnas.
df.isnull().sum()

# Ver valores '0' en cada una de las columnas.
print("Total presión: ", df[df.presion_sangre == 0].shape[0])
print("Total glucosa: ", df[df.glucosa == 0].shape[0])
print("Total piel: ", df[df.espesor_piel == 0].shape[0])
print("Total BMI: ", df[df.BMI == 0].shape[0])
print("Total insulina: ", df[df.insulina == 0].shape[0])

# Se eliminan las columnas 'espesor piel' y 'insulina', demasiados 0.
del df['espesor_piel']
del df['insulina']

df.to_csv(r'dataset\01_diabetes_manipulado.csv', index=False)
