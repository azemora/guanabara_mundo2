valor = 1
while True:
    valor = int(input('Digite o valor desejado: '))
    print('Tabuada')
    if valor < 0:
        print('Fim do programa.')
        break
    else:
        for i in range(10):
            print(f' {i} x {valor} = {valor * i}')

