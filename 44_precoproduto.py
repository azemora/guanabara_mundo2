while True:
    precoproduto = input('Digite o valor do produto: ')
    try:
        precoproduto = float(precoproduto)
        break
    except ValueError:
        print('Valor incorreto, informe o valor em reais: ')

print('Qual a forma de pagamento?')
valor_valido = [1, 2, 3, 4]
while True:
    print(" 1 - Dinheiro/Cheque \n 2 - Cartão \n 3 - 2x no Cartão \n 4 - 3x ou mais vezes no cartão ")
    valormenu = input()
    try:
        valormenu = int(valormenu)
        if valormenu in valor_valido:
            break
        else:
            print("valormenu inválido, digite novamente.")
    except ValueError:
        print("valormenu inválido, digite novamente.")

def switch_case(valormenu):
    if valormenu == 1:
        print(f'Opção em dinheiro ou cheque, total a pagar: R${precoproduto - (precoproduto * 0.1)}')
    elif valormenu == 2:
        print(f'Opção 1x no cartão, total a pagar: R${precoproduto - (precoproduto * 0.05)}')
    elif valormenu == 3:
        print(f'Opção 2x no cartão, total a pagar: R${precoproduto}')
    elif valormenu == 4:
        print(f'Opção 3x ou mais no cartão, total a pagar: R${precoproduto + (precoproduto * 0.2)}')      

switch_case(valormenu)