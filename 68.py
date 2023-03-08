import random
validos = ['PAR','IMPAR']
pcwin = 0
contador = 0
while pcwin == 0:
    jogada = int(input('Digite sua jogada: '))
    jogada2 = str(input('Você deseja par ou impar? ')).upper().strip()   
    jogadapc = random.randint(0,99)
    resultado = jogada + jogadapc
    if resultado % 2 == 0:
        if jogada2 == 'PAR':
            print(f'Você jogou {jogada}, o computador jogou {jogadapc}. O resultado é {resultado}. PAR. Você ganhou.')
            contador +=1
            print(f'Você ganhou {contador} vezes do computador.')
        else:
            print(f'Você jogou {jogada}, o computador jogou {jogadapc}. O resultado é {resultado}. PAR. Você perdeu.')
            print(f'Você ganhou {contador} vezes do computador.')
            pcwin +=1
    elif resultado %2 != 0:
        if jogada % 2 == 0:
            print(f'Você jogou {jogada}, o computador jogou {jogadapc}. O resultado é {resultado}. IMPAR. Você ganhou.')
            contador +=1
            print(f'Você ganhou {contador} vezes do computador.')
        else:
            print(f'Você jogou {jogada}, o computador jogou {jogadapc}. O resultado é {resultado}. IMPAR. Você perdeu.')
            pcwin +=1
            print(f'Você ganhou {contador} vezes do computador.')





