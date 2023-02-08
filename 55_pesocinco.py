
peso = float(input('Informe seu peso: '))
maior = peso
menor = peso
for i in range (0, 4):
    peso = float(input('Informe seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso foi: {maior}kg')
print(f'O menor peso foi: {menor}kg')