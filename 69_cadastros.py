
validos = ['S','N']
validos2 = ['F','M']
contadormais18 = homens = mulheres20 = contadorpessoas = 0
import sys
while True:
    print('--------- Cadastro da pessoas --------- ')
    while True:
        var1 = input('Deseja cadastrar uma pessoa? [s/n]').upper().strip()
        if var1 in validos:
            if var1 == 'S':
                break
            else:
                print('Resultado ------------')
                print(f'{contadorpessoas} pessoas cadastradas. \n{homens} homens cadastrados. \n{mulheres20} mulheres com menos de 20 anos cadastradas. \n---------------')
                sys.exit()
        else:
            print('Opção inválida, informe uma opção válida [s/n]')

    while True:
        sexo = input('Qual o sexo da pessoa? [M/F]').upper().strip()
        if sexo in validos2:
            if sexo == 'M':
                homens +=1
                break
            else:
                break
        else:
            print('Opção inválida, informe um sexo válido [f/m]')
    idade = int(input('Qual a idade da pessoa? '))
    contadorpessoas += 1
    if idade > 18:
        contadormais18 += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    