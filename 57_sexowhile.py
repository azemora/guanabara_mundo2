
while True:
    sexo = input('Digite seu sexo: \nM - Masculino \nF - Feminino ').strip()
    try:
        sexo = str(sexo)
        sexo = sexo.upper()
        if sexo == 'M':
            print('Masculino.')
        elif sexo == 'F':
            print('Feminino.')
        else:
            print('Sexo inválido, digite seu sexo corretamente.')
    except ValueError:
        print('Sexo inválido, digite seu sexo corretamente.')
