'''lista = list()
lista.append('hugo')
lista.append(37)
galera = list()
galera.append(lista[:])
lista[0] = 'bruno'
lista[1] = 27
galera.append(lista[:])
print(galera)'''
pessoa = list()
p = 0
dados = list()
while True:
    disciplina = str(input('Disciplina: '))
    if disciplina=='sair':
        break
    quantidade = int(input('numeros de alunos: '))
    if quantidade >= 1:
        for c in range(0, quantidade):
            dados.append(str(input('Nome: ')))
            dados.append(str(input('Idade: ')))
            pessoa.append(dados[:])
            dados.clear()
        print(pessoa)
    else:
        print('Numero inválido!')
print('fim')
