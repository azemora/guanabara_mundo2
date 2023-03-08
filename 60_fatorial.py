valor = int(input('Digite o valor: '))
fatorial = 1
for i in range(1, valor+1):
    fatorial = fatorial * i

print(f'Fatorial de {valor} é {fatorial}')