import sys
validos = [1,2,3,5]
valor1 = input('Informe o primeiro valor: ')
valor2 = input('Informe o segundo valor: ')

while True:
    print('Escolha uma opção:')
    operacao = int(input('1 - Somar \n2 - Multiplicar \n3 - Maior \n4 - Novos números \n5 - Sair do programa \n'))
    try:
       valor1 = int(valor1)
       valor2 = int(valor2)
       
       if operacao == 1:
            print(f'Operação de soma: {valor1} + {valor2} = {valor1+valor2}') 
       elif operacao == 3:
            if valor1 > valor2:
             print(f'Identificando o maior número entre: {valor1} e {valor2} = {valor1}')
            else:
             print(f'Identificando o maior número entre: {valor1} e {valor2} = {valor2}')
       elif operacao == 2:
            print(f'Operação de multiplicação: {valor1} * {valor2} = {valor1*valor2}')    
       elif operacao == 5:
        print('Fim do programa.')
        sys.exit() 
       elif operacao == 4: 
         valor1 = input('Informe o primeiro valor: ')
         valor2 = input('Informe o segundo valor: ')   
       else:
           print('Operação inválida')   
    except ValueError:
        print('Utilize valores inteiros.')
