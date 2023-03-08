import random

numeropc = random.randint(0,10)
contador  = 0

while True:
    jogada = input('Advinhe o número do computador(entre 0 - 10): ')
    contador = contador + 1
    try:
        jogada = int(jogada)
        if jogada == numeropc:
            print(f'Você acertou, você disse {jogada} e o número era {numeropc}. Foram {contador} tentativas.')
            break
        elif jogada < numeropc:
            print(f'Maior que {jogada}.')
        elif jogada > numeropc:
            print(f'Menor que {jogada}.')
        
    except:
        print('Tente novamente.')
