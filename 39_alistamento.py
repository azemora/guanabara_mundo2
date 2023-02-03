from datetime import datetime

anonascimento = int(input('Digite o seu ano de nascimento: '))

anoatual = datetime.now().year
idade = anoatual - anonascimento

if idade < 18:
    print(f'Você ainda não precisa se alistar, mas precisará em {18 - idade} ano(s)')
elif idade  >18:
    print(f'Você perdeu o alismento, está atrasado em {idade - 18} anos. ')
else:
    print('Você irá se alistar neste ano.')
