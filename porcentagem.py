'''efetuar reajuste de preço'''
valor = float(input('Informe valor: '))
reajuste = str(input('Informe se é ajuste [A] ou se é um desconto [B]: '))
taxa = float(input('Informe Taxa: '))
if reajuste == 'A':
    novo_valor = valor * (1 + (taxa/100))
    print(f'O valor {valor} reajuistado por +{taxa}/% é igual a {novo_valor:.2f}.')
elif reajuste == 'B':
    novo_valor = valor * (1 - (taxa/100))
    print(f'O valor {valor} descontado por -{taxa} é igual a {novo_valor:.2f}')
else:
    print('ERRO!')
