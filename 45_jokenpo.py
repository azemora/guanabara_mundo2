import random
jogadas_validas = [1,2,3]
print('Qual a sua jogada?')
print(" 1 - Pedra \n 2 - Papel \n 3 - Tesoura ")
while True:
    jogada = input()
    try:
        jogada = int(jogada)
        if jogada in jogadas_validas:
            break
    except ValueError:
        print('Jogada inválida, escolha uma das jogadas propostas. ')

jogada_pc =  random.choice(jogadas_validas)

'''
jogada = 1 
'''

if jogada == 1:
    print('Você escolheu pedra.')
    if jogada_pc == 1:
        print('Ambos escolheram pedra, o jogo empatou.')
    elif jogada_pc == 2:
            print('O computado escolheu papel, você perdeu.')
    else:
        print('O computador escolheu tesoura, você ganhou!')

if jogada == 2:
    print('Você escolheu papel.')
    if jogada_pc == 2:
        print('Ambos escolheram papel, o jogo empatou.')
    elif jogada_pc == 3:
         print('O computado escolheu tesoura, você perdeu.')
    else:
        print('O computador escolheu pedra, você ganhou!')

if jogada == 3:
    print('Você escolheu tesoura.')
    if jogada_pc ==3:
        print('Ambos escolheram tesoura, o jogo empatou.')
    elif jogada_pc == 2:
        print('O computado escolheu papel, você perdeu.')
    else:
        print('O computador escolheu pedra, você ganhou!')



  

