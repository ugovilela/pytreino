# se senao
# if objeto.caminho1():
#    bloo True
# else:
#     bloco False
tempo = int(input('Idade: '))
if tempo<=25:
    print('jovem')
else:
    print('Adulto')
print('-'*20)
# condições aninhadas
nome = str(input('Nome: '))
if nome == 'hugo':
    print('Bon Dia Hugo')
elif nome == 'pedro' or nome == 'lucas': #elif contração de else if
     n1 = str(input('quem está ai? '))
     print('bon dia \033[34m{}\033[m'.format(n1))
else:
     print('Acesso negado')



