def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
def soma(a,b):
    s = a + b
# empacotamento é receber diversos parametros 'def função(*núm)
def soma2(*valore):
    s = 0
    for num in valore:
        s += num
    print(f'somando os valore {valore} temos a soma {s}')


titulo('teste de função')
'''n1 = int(input('Valor de X: '))
n2 = int(input('Valor de Y: '))
n3 = int(soma(n1, n2))
print(f'O resultado da soma entre {n1} e {n1} é {n3}')'''
soma2(1, 2, 4)
soma2(2, 2)
help(print())
print(input.__doc__)
