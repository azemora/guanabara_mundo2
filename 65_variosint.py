resp = 'S'
soma = quant = media = 0

while resp in 'Ss':
    num = int(input('Digite o valor: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    resp =  str(input('Quer continuar? s/n')).upper().strip()[0]
media = soma/quant
print(f'Você digitou {quant}, numeros e media foi {media}')
print(f'O maior valor {maior}, menor {menor}')
