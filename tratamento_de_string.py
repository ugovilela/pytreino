''' ler uma frase e contar quantas letras e sua primeira e ultima posição'''
frase = str(input('Frase: ')).strip().upper()
letra = str(input('Digite letra a ser contada: ')).strip().upper()
contletra = pos = primeiro = posfinal = 0
for i in range(len(frase)):
    pos += 1
    if frase[i] == letra:
        contletra += 1
        posfinal = pos
        if contletra == 1:
            primeiro = i + 1
print(f'A quantidade de letra {letra} é {contletra}')
print(f'Primeira letra {letra} esta na posição {primeiro}')
print(f'Ultima letra {letra} esta na posição {posfinal}')

