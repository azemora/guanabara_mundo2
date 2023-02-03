print('Bem vindo á calculadora de empréstimos.')
valorimovel = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o valor do seu salário?'))
prazo = int(input('Em quantos anos deseja financiar a casa?'))

prazoemmeses = prazo * 12
#custo = (valorimovel)/(prazo * 12)

print(f'O imovél custará R${((valorimovel)/(prazo * 12)):.2f} por mês, durante {prazo *12} meses')
if (salario * 0.3) < (valorimovel)/(prazo * 12):
    print('Você não possui condições de financiar esse imóvel')
else:
    print('Parabéns, você pode financiar esse imóvel.')