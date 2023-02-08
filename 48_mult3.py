'''
soma = 0
for c in range (0, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            print(f"Número multiplico de 3: {c}")
            soma = soma +c

print(f"A soma de todos os números múltiplos de 3 \n Entre 0 e 500 é {soma}")
'''
contador = 0
soma = 0
for c in range (1, 501, 2):
        if c % 3 == 0:
            print(f"Número multiplico de 3: {c}")
            soma = soma +c
            contador = contador+1

print(f"A soma de todos os {contador} números múltiplos de 3 \n Entre 0 e 500 é {soma}")