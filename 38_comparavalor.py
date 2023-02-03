
while True:
    valor1 = input('Digite o primeiro valor: ')
    valor2 = input('Digite o segundo valor: ')
    try:
        valor1 = int(valor1)
        valor2 = int(valor2)
        break
    except ValueError:
        print("valor inválido, digite novamente.")

if valor1 == valor2:
    print('Valores iguais')
elif valor2 > valor1:
    print(f'Valor 2: {valor2} é maior que o Valor 1: {valor1}')
else:
    print(f'Valor 1: {valor1} é maior que o Valor 2: {valor2}')