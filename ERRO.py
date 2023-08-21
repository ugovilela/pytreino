try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Erro :( {erro.__class__}')
else:
    print((f'Resultado é {r}'))
finally:
    print('volte sempre')
