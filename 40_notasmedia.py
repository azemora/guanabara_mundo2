
while True:
    notas1 = input('Digite o valor da primeira nota: ')
    notas2 = input('Digite o valor da segunda nota: ')
    try:
        notas1 = float(notas1)
        notas2 = float(notas2)
        if 0.0 <= notas1 <= 10.0 and int(notas1) == notas1 and 0.0 <= notas2 <= 10.0 and int(notas2) == notas2:
            break
        else:
            print('Valores inválidos, digite novamente em formato decimal.')
    except ValueError:
        print('Números inválidos, digite novamente.')
media = (notas1 + notas2) / 2

if media >= 5.0 and media <= 6.9:
    print(f'Recuperação, média:{media}')
elif media >= 7.0:
    print(f'Aprovado, média:{media}')
else:
    print(f'Reprovado, média:{media}')