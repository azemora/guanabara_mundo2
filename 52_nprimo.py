valor_usuario = int(input('Informe um valor inteiro: '))
flag = True
for i in range (2, valor_usuario):
    if valor_usuario % i == 0:
        flag = False
        break

if flag:
    print('Número primo.')
else:
    print('Valor não é um número primo.')