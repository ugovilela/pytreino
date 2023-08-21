'''um número flutuante separar a parte inteira da fracionada'''
from math import trunc
numero = float(input('Digite um número: '))
print(f'Parte inteira: {trunc(numero)}')
