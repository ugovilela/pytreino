def somar(a=0, b=0, c=0):
    """
    -> Soma de três numeros com parametros
    opcinais
    :param a: Qualquer número interiro
    :param b: Qualquer número interiro
    :param c: Qualquer número interiro
    :return: sem retorno
    """
    s = a + b +c
    return s
    #print(f'Soma = {s}')
def comandos(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')


h = comandos(1, 10, 1)
#help(comandos)
retorno = 2 * somar(1, 1, 1)
print(f'valor do dobro da soma é {retorno}')

