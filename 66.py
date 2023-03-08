soma = valor = 0
contador = 0

while valor!= 999:
    valor = int(input('Digite o valor desejado: '))
    if valor == 999:
        break
    else:
        contador += 1
        soma += valor

print(f'Você digitou {contador} valores. A soma deles é {soma}')