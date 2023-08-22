''' ler nome completo, retornar o primeiro nome e o ultimo sobrenome'''
nome = str(input('Nome completo: ')).strip().upper()
vazio = ' '
contvazio = pos = primeiro = posfinal = 0
for i in range(len(nome)):
    pos += 1
    if nome[i] == vazio:
        contvazio += 1
        posfinal = pos
        if contvazio == 1:
            primeiro = i + 1
print(f'Primeiro nome: {nome[:primeiro]}')
print(f'Ultimo sobrenome: {nome[posfinal:]}')
