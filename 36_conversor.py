converter = int(input('Digite o número que deseja converter: '))
print('Qual base deseja converter?')

valor_valido = [1, 2, 3]
while True:
    print(f" 1 - Binário \n 2 - Octal \n 3 - Hexadecimal ")
    valormenu = input()
    try:
        valormenu = int(valormenu)
        if valormenu in valor_valido:
            break
        else:
            print("valormenu inválido, digite novamente.")
    except ValueError:
        print("valormenu inválido, digite novamente.")

if valormenu == 1:
    print(bin(converter))
elif valormenu == 2: 
    print(hex(converter))
elif valormenu == 3:
    print(oct(converter)) 