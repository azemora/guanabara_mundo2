nomevelho = ''
mediaidade = 0
maioridade = 0
numeromulheres = 0

for i in range (0, 4):
    nome = str(input('Informe o seu nome: '))
    sexo = int(input('Informe seu sexo: \n 1 - Masculino \n - 2 Feminino \n'))
    idade = int(input('Informe sua idade: '))
    mediaidade = mediaidade + idade
    if sexo == 1 and idade > maioridade:
        maioridade = int(idade)
        nomevelho = nome
    if sexo == 2 and idade < 20:
        numeromulheres = numeromulheres+1

print(f"O homem mais velho se chama: {nomevelho}")
print(f'A idade média das pessoas é de : {mediaidade/4}')
print(f'{numeromulheres} mulheres tem menos de 20 anos.')

