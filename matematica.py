#import emoji
import math
# ou from math import srqt
# ai raizx = sqrt(x)
#print(emoji.emojize("ola mundo :earth_americas:", language='alias'))
print('\033[33mOlá mundo\033[m')
print('\033[1;32mOlá mundo\033[m')
print('\033[4;35;40mOlá mundo\033[m')
n1 = input('digite o seu nome: ')
print(n1, type (n1))
x = int(input('valor de x = '))
y = int(input('o valor de y = '))
soma = x + y
multiplicacao = x * y
divizao = x / y
potencia = x ** y
divizaoint = x // y
modulorestodiv = x % y
print('A soma {}, multiplicação {}, divisão {:.2f}, potencia {},'
      'divisão inteira {}, modulo {}'.format(soma, multiplicacao, divizao, potencia, divizaoint, modulorestodiv))
print('='*20)
raizx = math.sqrt(x)
raizy = math.sqrt(y)
print('a raiz quadrada de x é {:.2f} e de y é {:.2f}'.format(raizx, raizy))
print('='*20)

