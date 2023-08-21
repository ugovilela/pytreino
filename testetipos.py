'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informaçoes ´possiveis sobre ele.'''
tipo = input('Digite tipo: ')
print(f'O tipo <{tipo}> é {type(tipo)}')
print(f'só tem espaços?', tipo.isspace())
print(f'e só espaço? {tipo.isspace()}')


