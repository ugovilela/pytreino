'''TABUADA'''
numero = int(input('Digite um numero: '))
print('-' * 20)
for c in range(1, 11):
    multiplicação = numero * c
    print(f'{numero:2} X {c:2} = {multiplicação:2}')
print('-' * 20)