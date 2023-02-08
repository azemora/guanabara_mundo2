
while True:
    valor_usuario = input('Digite um valor: ')
    try:
        valor_usuario = int(valor_usuario)
        break
    except ValueError:
        print("Valor inválido, por favor informe um valor inteiro.")

print("Tabuada:")
for c in range (0, 10):
    print(f"{c} x {valor_usuario} = {c*valor_usuario}")