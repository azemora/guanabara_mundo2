valor = int(input('Digite o valor desejado: '))
termo = 0
penultimo = 1
ultimo  = 0
count = 0

if valor >= 2:
    for i in range(0, valor):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
            


