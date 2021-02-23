# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:57:04 2021

@author: PedroLuis
"""
import math

print('Hola Mundo')

a = 5
print(a)

# suma
a = 5
b = 2
c = a+b
print(c)

# resta
a = 5
b = 2
c = a-b
print(c)

# multiplicacion
a = 5
b = 2
c = a*b
print(c)

# division
a = 5
b = 2
c = a/b
print(c)

# division parte entera
a = 5
b = 2
c = a//b
print(c)

# potencia
a = 5
b = 2
c = a**b
print(c)

# raiz cuadrada
a = 16
b = a ** (1/2)
print(b)

# raiz con importacion
raiz = math.sqrt(25)

# TIPOS DE DATOS
a = 5
print(type(a))
print(a)
a = "hola"
print(type(a))
print(a)
a = 4.5
print(type(a))
print(a)
a = True
print(type(a))
print(a)


# String str
a = "hola mundo"
b = 'hola mundo'
c = "I cant't do it"
d = 'Alias "Carlos"'

# Enteri int
a = 5

# Decimal float
x = 3.5

# Booleano bool
x = True
x = False

# Conversion de Strin a Entero
x = '3'
y = int(x)
print(y)

# Conversion de String a Decimal
x = 3
y = float(x)
print(x)

# Conversion de decimal a String
x = 3.5
y = str(x)
print(y)

# Concatenaciones

a = 'hola'
b = 'Carlos'
c = a + ' ' + b
print(c)

a = 'Roberto'
b = 5
c = a * 5
print(c)


# CAPTURA DE DATOS POR PANTALLA

nombre = input('Digite su nombre: ')
print(nombre)

print('Digite su nombre: ')
nombre = input()
print(nombre)

# Algotimo que sume dos numeros e imprima su resultado
num_uno = input('Digite el número uno: ')
num_dos = input('Digite el número dos: ')
suma = num_uno + num_dos
# print('La suma es', suma)
print(f'La suma es {suma}')


# Algoritmo que lea un numero y lo eleve al cuadrado
num_uno = int(input('Digite el número a elevar: '))
r = num_uno ** 2
print(f'El cuadrado del {num_uno} es: {r}')


# Algoritmo que tome el valor de un producto y le
# aplique el 20" de descuento, imprima el valor del
# producto inicial, el valor del producto con descuento
# y el valor ahorrado

vp = float(input('Digite el valor del producto: '))
vd = vp * 0.2
vpg = vp - vd
print(f'El valor del prodcto es; ${vp:,}')
print(f'El valor con descuento es: ${vpg:,}')
print(f'El descuento es: ${vd:,}')

# CONDICIONALES

# Tabla de verdad del ad
# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabla de verdad del or
# v and v = v
# v and f = v
# f and v = v
# f and f = f

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negacion
print(not True)
print(not False)

# Mas de dos condiciones al mismo tiempo
print(True and False and True or False or True and True)
print(True and (False and True) or (False or True) and True)

# Jerarquia de Operaciones
# 1. pARENTTESIS Y LLAVES
# 2. Potencias y Reices
# 3. Multiplicaciones y Divisiones
# 4. Sumas y restas

# Jerarquiera de operaciones boleanas
# 1. Parentesis y llaves
# 2. Tabla de verdad binaria


# Estructura de un if
if(x > 0):
    print('Positivo')
else:
    print('Negativo')
print('Resultado')

# Algoritomo que dada la edad de una persona diga si es mayor
# o menor de edad
edad = int(input('Digite la edad: '))
if(edad >= 18):
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

# Algoritmo que dado un numero N diga si es negativo
# positivo o cero

n = int(input('Digite el número'))
if n == 0:
    print('El número es cero')
elif n > 0:
    print('El número es positivo')
else:
    print('El número es negativo')
