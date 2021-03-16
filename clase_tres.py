# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:15:52 2021

@author: PedroLuis
"""

# Ejercicio 1 vectores
# Algoritmo dado un conjunto de nueros ingresados por el usuario
# indique cuanos de estos son pares, empleando vectores

# Capturar cantidad de elementos
cant_numeros = int(input('Digite la cantidad de números a ingresar: '))
numeros = []

# Capturar los números
for i in range(1, cant_numeros + 1):
    num = int(input(f'Digite el número {i}: '))
    numeros.append(num)
print(f'Los números ingresados fieron: {numeros}')

# Recorridos de los vectores
cont_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        cont_pares += 1
print(f'La cantidad de números pares ingresador fue: {cont_pares}')


# Version 2 del mismo ejercicio anterior
i = 1
numeros = []
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    # value_when_true if condition else value_when_false
    # If condition: code
    if num == 0: break
    i += 1
print(f'Los números ingresados fieron: {numeros}')

# Recorridos de los vectores
cont_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        cont_pares += 1
print(f'La cantidad de números pares ingresador fue: {cont_pares}')


# Ejercicio 2
# Algoritmo que dado un vector de numeros los devuelva ordenados
# y que no esten repetidos
i = 1
numeros = []
while True:
    num = int(input(f'Digite el número {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    i += 1
print(f'Los números ingresados fieron: {numeros}')

# Recorridos de los vectores
numeros_ord = list(set(numeros))
print(f'El vector ordenado y sin repetidos es: {numeros_ord}')


# Funcines
# Parametros opcionales
def saludar(nombre='Mundo'):
    print(f'Hola {nombre}')


# Parametros obligatorios
def saludar2(nombre):
    print(f'Hola {nombre}')


def saludar3(nombre1, nombre2, nombre3):
    print(f'Hola {nombre1}')
    print(f'Hola {nombre2}')
    print(f'Hola {nombre3}')


def saludar4(nombre1, nombre2, nombre3='Carlos'):
    print(f'Hola {nombre1}')
    print(f'Hola {nombre2}')
    print(f'Hola {nombre3}')


# Parametros infinitos
# Arguments
def saludar5(*nombres):
    for nombre in nombres:
        print(f'Hola {nombre}')


# Keywords argument
def saludar6(**nombres):
    print(nombres)
