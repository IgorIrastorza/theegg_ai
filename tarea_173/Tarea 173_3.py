# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:10:21 2022

@author: igori
"""

import pandas as pd

'''
SIGNIFICADO COLUMNAS DATAFRAME
1.- Survived (0 = No; 1 = Yes): Supervivientes
2.- Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd): Clase
3.- Name: Nombre
4.- Sex: Sexo
5.- Age: Edad
6.- Number of Siblings/Spouses: Hermanos/Cónyuges
7.- Number of Parents/Children: Padres/Hijos
8.- Ticket: Ticket
9.- Passenger Fare: Tarifa de pasajero
10.- Cabin: Cabina
11.- Embarked (C = Cherbourg; Q = Queenstown; S = Southampton): Embarcado
'''

df = pd.read_csv('dataset/02_titanic.csv')
df.dtypes
df.info()
df.describe()  # Breve descripción del dataframe.
df.corr()  # Matriz de correlación, en formato número.
df.columns  # Para ver los nombres de las columnas.

# Mayor superviviencia de mujeres respecto a hombres.
sex_survrate = df.groupby(['Survived', 'Sex']).count()
print('----------------------------------------------------------------------')
print("Supervivencia femenina: %", sex_survrate.iloc[2, 0] /
      (sex_survrate.iloc[0, 0]+sex_survrate.iloc[2, 0]))
print("Supervivencia masculina: %", sex_survrate.iloc[3, 0] /
      (sex_survrate.iloc[1, 0]+sex_survrate.iloc[3, 0]))

# Mayor supervivencia en asientos de 1. y 2. clase (correlación negativa).
pclass_survrate = df.groupby(['Survived', 'Pclass']).count()
print('----------------------------------------------------------------------')
print("Supervivencia 1. clase: %", pclass_survrate.iloc[3, 0] /
      (pclass_survrate.iloc[0, 0]+pclass_survrate.iloc[3, 0]))
print("Supervivencia 2. clase: %", pclass_survrate.iloc[4, 0] /
      (pclass_survrate.iloc[1, 0]+pclass_survrate.iloc[4, 0]))
print("Supervivencia 3. clase: %", pclass_survrate.iloc[5, 0] /
      (pclass_survrate.iloc[2, 0]+pclass_survrate.iloc[5, 0]))

df.isnull().sum()
del df['Cabin']  # Demasiados valores nulos, no aporta nada.
del df['Age']  # Muchos valores nulos, pero podría ser un dato intersante.
del df['Ticket']  # No aporta nada.
del df['Name']  # No aporta nada.

df['Embarked'] = df['Embarked'].replace(['S', 'C', 'Q'], [0, 1, 2])
df['Sex'] = df['Sex'].replace(['female', 'male'], [0, 1])

df.corr()  # Calcular de nuevo las correlaciones despues de las correcciones.

df.to_csv(r'dataset\02_titanic_manipulado.csv', index=False)
