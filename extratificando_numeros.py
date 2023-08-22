numero = str(input('Numero: ')).strip()
compara = len(numero)

if compara == 1:
        print(f'{numero} unidades\n'
              f'0 dezenas\n'
              f'0 centenas\n'
              f'0 milhares')
elif compara == 2:
        print(f'{numero[1]} unidades\n'
              f'{numero[0]} dezenas\n'
              f'0 centenas\n'
              f'0 milhares')
elif compara == 3:
        print(f'{numero[2]} unidades\n'
              f'{numero[1]} dezenas\n'
              f'{numero[0]} centenas\n'
              f'0 milhares')
elif compara ==4:
    print(f'{numero[3]} unidades\n'
          f'{numero[2]} dezenas\n'
          f'{numero[1]} centenas\n'
          f'{numero[0]} milhares')
else:
        print(f'{numero[compara - 1]} unidades\n'
              f'{numero[compara - 2]} dezenas\n'
              f'{numero[compara - 3]} centenas\n'
              f'{numero[compara - 4]} milhares')
print('FIM')