''' faser um programa que calcula multa '''
print('Bom dia.')
credito = int(input('Pontos: '))
velocidade = 0
while True:
    velocidade = int(input('Velocidade: '))
    if velocidade == 0 or credito <= 0:
        break
    elif velocidade <= 80:
        print(f'\033[32mVeocidade segura\033[m')
    elif 80 <= velocidade <= 100:
        print(f'\033[33mVelocidade Insegura\033[m')
    elif velocidade > 100:
        credito = credito - 3
        print(f'\33[31mPerigo\33[m')
        print(f'Credito {credito}')
print(f'Carro Parado')