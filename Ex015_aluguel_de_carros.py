'''Um programa que pergunte km rodados e
dias alugados e retorne o valor a ser pago'''
km = float(input('Kilometros rodados: '))
dias = int(input('Dias alugados: '))
cobranca = km * 0.75 + dias * 50
print(f'Total a pagar: R$ {cobranca:.2f}')


