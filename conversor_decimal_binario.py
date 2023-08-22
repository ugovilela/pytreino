'''converso decimal binario'''
decimal = int(input('Numero decimal inteiro: '))
binario = ' '
while True:
    resto = decimal % 2
    binario += str(resto)
    decimal //= 2
    if decimal == 0:
        break
binario = binario[::-1]
#print(f'{divisao}')
#print(f'{resto}')
print(f'{binario}')