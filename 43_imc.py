while True:
    altura = input('Informe a sua altura em metros: ')
    peso = input('Informe o seu peso em kg: ')
    try:
        altura = float(altura)
        peso = float(peso)
        break
    except ValueError:
        print('Valores inválidos, informe corretamente. ')

imc = (peso/(altura ** 2))

def switch_case(imc):
    if imc <= 18.5:
        print('Categoria: ABAIXO DO PESO')
    elif 18.5 <= imc <= 25:
        print('Categoria: PESO IDEAL')
    elif 25 <= imc <= 30:
        print('Categoria: SOBREPESO')
    elif 30 <= imc <= 40:
        print('Categoria: OBESIDADE')       
    else:
        print('Categoria: OBESIDADE MÓRBIDA')

switch_case(imc)