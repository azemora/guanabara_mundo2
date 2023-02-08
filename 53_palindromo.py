import string

vusuario = str(input('Digite a string para verificar se é um palindromo: '))
semespaco = vusuario.replace(" ", "")
stamanho = len(semespaco)

if semespaco == semespaco[::-1]:
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")