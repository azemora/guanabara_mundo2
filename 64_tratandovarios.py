valor = 0
cont = 0
soma = 0 

while valor != 999:
    valor = int(input('Digite 999 para parar: '))
    if valor != 999:
        soma += valor
        cont += 1
print((f'Você digitou {cont} vezes, a soma desses valores é {soma}'))