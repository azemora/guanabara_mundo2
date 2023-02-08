soma = 0
for i in range (6):
    valor = int(input('Digite seis valores inteiros: '))
    if valor % 2 == 0:
        soma = soma+valor
        print(f'Valor par ({valor}), adicionado á soma: {soma}')
        