''' Faça um programa que retorne o antecessor e o posterior de um nuemero'''
try:
    entrada = int(input('Digite um numero inteiro: '))
    anterior = entrada - 1
    posterior = entrada + 1
except Exception as erro:
    print(f'ERRO :( {erro.__class__}')
else:
    print(f'Para o úmero {entrada} tem como anterior {anterior} e posterior {posterior}')
finally:
    print('Fim')
