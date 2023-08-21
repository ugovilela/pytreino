'''for c in range(0, 10, 2):
    print(c)
print('FIM')
ex = 1
while ex != 0:
    ex = int(input('Digite um valor: '))
print('fim')'''
# com parada
n = s = 0
while True:
    n = int(input('Número: '))
    if n == 00:
        break
    s += n
print('A soma dos valores é {}'.format(s))
print(f'A soma vale {s}')

