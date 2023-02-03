'''
while True:
    lado1 = input('Digite o tamanho do lado primeiro lado: ')
    lado2 = input('Digite o tamanho do lado segundo lado: ')
    lado3 = input('Digite o tamanho do lado terceiro lado: ')

    try:
        lado1 = float(lado1)
        lado2 = float(lado2)
        lado3 = float(lado3)
        break
    except ValueError:
        print('Números inválidos, digite novamente.')
'''
lado1 = str(input('Digite o tamanho do lado primeiro lado: '))
lado2 = str(input('Digite o tamanho do lado segundo lado: '))
lado3 = str(input('Digite o tamanho do lado terceiro lado: '))

if lado1 == lado2 == lado3:
    print('Triângulo Equilátero')
elif lado1 == lado2 or lado3 == lado1 or lado2 == lado3:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')