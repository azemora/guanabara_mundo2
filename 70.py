import sys
somavalor = contador100 = 0
validos = ['S','N']
produtobarato = 0
produtonome = 0 
flagatri = False
while True: 
    while True:
        opcao = str(input('Deseja cadastrar um novo produto?[s/n] ')).upper().strip()
        if opcao in validos:
            if opcao == 'S':
                break
            else:
                print(f'`Valor total: R${somavalor:.2f} \n{contador100} Produtos a cima de R$1000,00. \nProduto mais barato: {baratonome}')
                sys.exit()
    nome = str(input('Qual o nome do produto? '))
    while True:
        valor = input('Qual o valor? ')
        if valor.isnumeric():
            valor = float(valor)
            if flagatri == False:
                produtobarato = valor
                flagatri = True
                baratonome = nome
            somavalor += valor
            if valor > 1000:
                contador100 += 1
            break
        else:
            print('Informe o valor correto.')
    
    if valor < produtobarato:
        produtobarato = valor
        baratonome = nome

    
