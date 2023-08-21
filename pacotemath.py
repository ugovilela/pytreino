''' operadores aritimeticos'''
from math import sqrt
def dobro(n):
    n *= 2
    return(n)


print('Entrada de dados')
numero = float(input('Núnero: '))
print('*' * 50)
print('Execução')
raiz = sqrt(numero)
dobro = dobro(numero)
print(f'Número {numero}\n'
      f'Raiz quadrada {raiz:.2f}\n'
      f'Dobro {dobro}')




