while True:
    idade = input('Digite sua idade: ')
    try:
        idade = int(idade)
        if idade >= 0 and int(idade) == idade:
            break
        else:
            print('Idade inválida, digite a idade corretamente.')
    except ValueError:
        print('Idade inválida, digite a idade corretamente.')

def switch_case(idade):
    if idade <= 9:
        print('Categoria: MIRIM')
    elif 10 <= idade <= 14:
        print('Categoria: INFANTIL')
    elif 14 <= idade <= 19:
        print('Categoria: JUNIOR')
    elif 14 <= idade <= 19:
        print('Categoria: SENIOR')       
    else:
        print('Categoria: MASTER')

switch_case(idade)