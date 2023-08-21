'''Calcular media de uma lista'''
contador = soma = 0
while True:
    numero = float(input('Digite um número: '))
    if numero == 00:
        break
    else:
        contador += 1
        soma += numero

#media = soma / 5
print('fim')
print(soma)
print(f'Media {soma/contador}')
