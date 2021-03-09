# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:08:02 2021

@author: PedroLuis
"""

# Ciclo for

for valor in range(10):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(2, 100, 2):
    print(valor)

for i in range(1, 11):
    for j in range(1, 6):
        print(i, j)


# Ciclo While

while True:
    print("hola")
    break

i = 2
while i <= 10:
    print(i)
    # i = i + 2
    i += 2


# Algoritmo que imprima el ganador de una eleccion de dos candidatos

nvotos = int(input('Digite la cantidad de votos: '))

uno = 0
dos = 0
for n in range(1, nvotos+1):
    candidato = input('Digite 1 para candidato A o digite 2 para el B: ')
    if candidato == 1:
        uno += 1
    else:
        dos += 1
if uno > dos:
    print(f'gano candidato uno 1 con {uno} votos ')
elif dos > uno:
    print(f'Gano candidato dos 2 con {dos} votos ')
else:
    print("Se presento un empate")


# Algoritmo que de las n notas de un estudiante calcule el primedio
nnotas = int(input('Digite la cantidad de notas: '))
r = 0
for i in range(1, nnotas+1):
    while True:
        no = float(input('Digite la nota: '))
        if no >= 0 and no <= 5:
            break
    r += no
t = r / nnotas
print(f'El promedio es: {t}')


# Tipos de colecciones

# Listas o vectores
# Tipo de dato mutable y ordenado

a = [2, 3, 4, 6, 3]
b = [2, True, 'hola', 3.4]
c = [2, [True, False], ['hola', 'mundo'], [2.3, 3.4, 4.6, 7.8]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)

a[0] = 7
print(b[2])
a = [2, 3, 4, 6, 3]
a.append(5)  # Agrega el elemento al final de la lista
print(a)

a.remove(3)  # Elimina de la lista un elemento por su valor

a.pop()  # Elimina el ultimo elemento del vector

a.pop(1)  # Elimina un elemento por posicion

a.clear()  # Elimina todo los elementos del vector

# del a   Elimina todo el arreglo

4 in a  # Busca el elemento 4 dentro de a

len(a)  # Cantidad de elementos de la lista

id(a)  # Convierte en decimal la direccion en memoria de un objeto

b = a[:]  # Copia de los elementos
a.copy(a)

c = b[0:3]
c = b[:3]
c = b[2:]

# Tuplas
# Tipo de dato inmutable y ordenado

a = (1, 2, 3, 4)
print(a[1])
a = (1, 'Hola', True, 4.5)
a = (1, ['Hola', 'Mundo'], True, 4.5)
a = (1, ['Hola', 'Mundo'], (True, False), 4.5)
b = a[:2]
4 in a
# del a PUEDO BORRAR DATO DE LA RAM


# Set
# Tipos de datos mutables y no ordenados
a = {1, 2, 3, 4}
a = {7, 2, 1, 5, 9}

# Diccionario
# Mutable pero no ordenado
a = {'nombre': 'Pedro', 'apellido': 'Marchena'}
a = {'1': 'Pedro', '2': 'Marchena'}

a['nombre']
a['nombre'] = 'Carlos'


# Funciones
def nombre_funcion():
    pass


def hola_mundo():
    print('Hola mundo')


def saludo(nombre='Mundo'):
    print(f'Hola {nombre}')


def suma(num1, num2):
    return num1 + num2


def operaciones(num1, num2):
    su = num1 + num2
    re = num1 - num2
    mu = num1 * num2
    di = round(num1 / num2, 2)
    return su, re, mu, di


resultados = operaciones(4, 5)
su, re, mu, di = resultados
_, _, _, div = resultados
