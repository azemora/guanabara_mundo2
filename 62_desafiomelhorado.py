
valor = int(input('Quantos valores de fibonnaci vc deseja ver: '))
a = 0
b = 1
cont = 1
while cont <= valor:
    c = a+b
    a = b
    b = c
    cont +=1
    print(c)
print('Fim')

 