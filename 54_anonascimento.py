
maiores = 0
menores = 0
for i in range (0, 7):
    while True:
        idade = input('Digite a sua idade: ')
        try:
            idade = int(idade)
            break
        except ValueError:
            print("idade inválido, digite novamente.")
    
    if idade >= 18:
        maiores = maiores+1
    else:
        menores = menores+1

print(f'{maiores} pessoas maiores idades')
print(f'{menores} pessoas menor idades')

